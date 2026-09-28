# Azure Data Table Logging

A Python package that simplifies logging into Azure Data Tables.

## Features

- Stores Python log events in Azure Data Tables.
- Automatically creates the table if it does not already exist.
- Supports standard logging levels such as `DEBUG`, `INFO`, `WARNING`, and `ERROR`.

## Prerequisites

- Python 3.12 or higher
- An Azure Storage Account
- An access key for the storage account

## Installation

Install the package from PyPI:

```bash
pip install azt-logging
```

## Example Usage

```python
import os

from azt_logging import create_logger

logger = create_logger(
    st_account_name=os.environ["AZURE_STORAGE_ACCOUNT_NAME"],
    account_key=os.environ["AZURE_STORAGE_ACCOUNT_KEY"],
    table_name="application_logs",
)

logger.info("Application started.")
logger.warning("This is a warning.")
logger.error("Something went wrong.")
```

Keep your Azure account key in an environment variable instead of placing it directly in source code.

## Known Limitations

If an Azure table with the specified name is currently being deleted, Azure may return a `TableBeingDeleted` error until the deletion has completed.

## License

This project is licensed under the [MIT License](LICENSE).
