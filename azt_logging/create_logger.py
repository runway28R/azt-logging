import logging

from .table_log_handler import table_logger


def create_logger(
    st_account_name: str,
    account_key: str,
    table_name: str,
    log_level: int = logging.INFO,
) -> logging.Logger:
    """
    Creates a logger that stores records in an Azure Table Storage table.

    Args:
        st_account_name (str): Azure Storage account name.
        account_key (str): Azure Storage account access key.
        table_name (str): Name of the Azure Table Storage table.
        log_level (int): Logging level, such as logging.INFO or logging.DEBUG.

    Returns:
        logging.Logger: A configured logger that writes records to Azure Table Storage.
    """
    azure_logger = table_logger(
        st_account_name=st_account_name,
        account_key=account_key,
        table_name=table_name,
        log_level=log_level,
    )

    return azure_logger.get_logger()
