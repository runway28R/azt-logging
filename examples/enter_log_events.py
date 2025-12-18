from azt_logging.table_log_handler import table_logger
import argparse


def store_log_entry():
    """
    Parse st_account_name, account_key and table_name from CLI and make demo entries in the table.
    """
    parser = argparse.ArgumentParser(description="Upload a file to SharePoint using Microsoft Graph.")
    parser.add_argument("--st_account_name", required=True, help="Azure Storage Account Name", type=str)
    parser.add_argument("--account_key", required=True, help="Azure Storage Account Access Key", type=str)
    parser.add_argument("--table_name", required=True, help="Table Name within that Storage Account", type=str)
    parser.add_argument("--log_level", required=False, default=10, help="Log Level (e.g., 10 for DEBUG, 20 for INFO)", type=int)

    args = parser.parse_args()

    azt_logger_handler = table_logger(st_account_name=args.st_account_name,
                                   account_key=args.account_key,
                                   table_name=args.table_name,
                                   log_level=args.log_level)


    azt_logger = azt_logger_handler.get_logger()
    azt_logger.debug("This is a DEBUG log entry.")
    azt_logger.info("This is an INFO log entry.")
    azt_logger.warning("This is a WARNING log entry.")
    azt_logger.error("This is an ERROR log entry.")
    azt_logger.critical("This is a CRITICAL log entry.")


if __name__ == "__main__":
    store_log_entry()