from bot.config.constants import TgBot
from bot.config.logger_builder import build_logger


logger = build_logger(__name__)


async def drop_messages(chat_id: int, message_list: list[int]) -> None:
    for message_id in range(message_list[0], message_list[-1] + 1):

        try:
            await TgBot.bot.delete_message(chat_id=chat_id, message_id=message_id)

        except Exception as e:
            logger.info(f"Bot cannot drop message with {id} id. -> {e}")


async def drop_message(chat_id: int, message_id: int) -> None:
    try:
        await TgBot.bot.delete_message(chat_id=chat_id, message_id=message_id)

    except Exception as e:
        logger.info(f"Bot cannot drop message with {id} id. -> {e}")
