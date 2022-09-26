import re


def make_customer_string(data: dict) -> str:
    """Make user string to write it into database as quote author."""
    first_name = data.get("first_name", None)
    last_name = data.get("last_name", None)
    username = data.get("username", None)

    final = f"{first_name} {last_name} aka. @{username}"

    final = re.sub(r"(None|aka. @None)", "", final)  # Clean None
    final = re.sub(r"\s+", " ", final)  # Clean extra spaces
    final = re.sub(r"^\s+|\s+$", "", final)  # Clean hanging spaces

    return final if final else "Unknown user"
