# Azure Data Table Logging

A Python package that simplifies logging into Azure Data Tables. 

## Current Features
- **Logging**: Python logger to store events into Azure Data Tables

## Prerequisites

- Python 3.14 or higher (lower versions may work but are not tested)
- Azure Storage Account
  - Access Key for that Storage Account

## Installation

```bash
# Clone the repository
git clone https://github.com/runway28R/azt-logging.git
cd azt-logging

# Install required packages
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

#### Features

- Logging into a table in Azure Data Tables. If a table does not exist, it will get created.

#### Example Usage

```bash
# Create sample log entries
python -m examples.enter_log_events 
--st_account_name STORAGE_ACCOUNT_NAME 
--account_key STORAGE_ACCOUNT_KEY 
--table_name TABLE_NAME 
--log_level 10  
```

#### Unhandled Exceptions

- TableBeingDeleted Error: In a case where the tbale with specified name is being deleted, but deletion of it hasn't completed yet, the code will fail.
