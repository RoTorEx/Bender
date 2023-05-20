from datetime import datetime, timezone

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.config import read_config
from src.config import build_logger


config = read_config()
logger = build_logger(__name__)


class AwardsService:
    def __init__(self) -> None:
        # Google API
        self.google_sheet_id = config.google.sheet_id
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        self.service_account_file = "keys/service_account.json"
        # Sheet
        self.table_name = "Award"
        self.left_column = "A"
        self.right_column = "P"
        self.line = ""
        self.sheet_range = f"{self.table_name}!{self.left_column}{self.line}:{self.right_column}{self.line}"

    async def get_data_from_sheet(self) -> None:
        service = await self._build_service()

        try:
            result = (
                service.spreadsheets()
                .values()
                .get(spreadsheetId=self.google_sheet_id, range=self.sheet_range)
                .execute()
            )

            values = result.get("values", [])
            logger.info(f"{len(values)} rows read from {self.sheet_range}")
            logger.info(f"{values = }")

        except HttpError as error:
            logger.error(f"An error occurred: {error}")

    async def write_data_in_sheet(self, message_text: str) -> None:
        service = await self._build_service()

        now = datetime.now(timezone.utc)
        formatted_date = now.strftime("%Y-%m-%d")

        message_array = message_text.split("\n")
        data_array = [formatted_date]

        data_array.extend(message_array)

        try:
            request = (
                service.spreadsheets()
                .values()
                .append(
                    spreadsheetId=self.google_sheet_id,
                    range=self.sheet_range,
                    valueInputOption="USER_ENTERED",
                    insertDataOption="INSERT_ROWS",
                    body={"values": [data_array]},
                )
                .execute()
            )
            logger.info(f'{request.get("updates").get("updatedCells")} cells appended to {self.sheet_range}')

        except HttpError as error:
            logger.error(f"An error occurred: {error}")

    async def _build_service(self):
        creds = None

        try:
            creds = service_account.Credentials.from_service_account_file(self.service_account_file, scopes=self.scopes)

        except FileNotFoundError:
            logger.error(f"The service account file {self.service_account_file} was not found.")

        return build("sheets", "v4", credentials=creds)
