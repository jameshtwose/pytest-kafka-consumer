"""This module contains the business logic for the consumer application.

- add_timezone_info: Adds timezone information to a datetime string.
- convert_money_int_to_str: Converts an integer representing money to a string.
- convert_to_lower_case: Converts a string to lower case.
- message_processing_pipeline: Processes a message according to the business logic.

"""

from typing import Any
import datetime
from zoneinfo import ZoneInfo
import logging
from consumer.utils import create_filled_jinja_template

logger = logging.getLogger(__name__)

EUROPE_AMSTERDAM = ZoneInfo("Europe/Amsterdam")

def add_timezone_info(datetime_str: str) -> str:
    """This function adds timezone information to a datetime string.

    Parameters
    ----------
    datetime_str : str
        A datetime string in the format 'YYYY-MM-DD HH:MM:SS'.

    Returns
    -------
    str
        The datetime string with timezone information appended.
    """
    try:
        datetime_obj = datetime.datetime.fromisoformat(datetime_str)
        # Add timezone information
        datetime_obj = datetime_obj.replace(tzinfo=EUROPE_AMSTERDAM)
        return datetime_obj.isoformat()
    except ValueError as e:
        raise ValueError(f"Invalid datetime string: {datetime_str}") from e
    
def convert_money_int_to_str(money_int: int) -> str:
    """This function converts an integer representing money to a string.

    Parameters
    ----------
    money_int : int
        The integer representing money.

    Returns
    -------
    str
        The money as a string.
    """
    try:
        return f"${money_int:.2f}"
    except ValueError as e:
        raise ValueError(f"Invalid money integer: {money_int}") from e
    
def convert_to_lower_case(s: str) -> str:
    """This function converts a string to lower case.

    Parameters
    ----------
    s : str
        The string to convert to lower case.

    Returns
    -------
    str
        The string in lower case.
    """
    try:
        return s.lower()
    except AttributeError as e:
        raise AttributeError(f"Invalid string: {s}") from e
    
def message_processing_pipeline(message: dict[str, Any]) -> dict[str, Any]:
    """This function processes a message according to the business logic.

    Parameters
    ----------
    message : Dict[str, Any]
        The message to process.

    Returns
    -------
    Dict[str, Any]
        The processed message.
    """
    logger.info(f"Received message: {message}")
    if message.get("history").get("last_login"):
        message["history"]["last_login"] = add_timezone_info(
            message.get("history").get("last_login")
        )
        for purchase in message.get("history").get("purchase_history"):
            purchase["purchase_date"] = add_timezone_info(
                purchase["purchase_date"]
            )
            purchase["amount"] = convert_money_int_to_str(purchase["amount"])
            purchase["item_name"] = convert_to_lower_case(purchase["item_name"])
        
        logger.info(f"Processed message: {message}")
        filled_yaml = create_filled_jinja_template(message)
        logger.info(f"Filled yaml:\n\n{filled_yaml}")
        
        return message