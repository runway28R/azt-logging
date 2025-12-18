import logging
from socket import gethostname
from azure.data.tables import TableServiceClient


class table_logger:
    def __init__(self, st_account_name, account_key, table_name, log_level):
        #logger.setLevel(logging.DEBUG)
        #debug=10
        #info=20
        #warning=30
        #error=40
        #critical=50
        
        self.logger = logging.getLogger(table_name)
        self.logger.setLevel(int(log_level))

        # Clear existing handlers to avoid duplicate logs
        if len(self.logger.handlers) > 0:
            self.logger.handlers.clear()

        log_handler = table_handler(st_account_name=st_account_name,
                                            account_key=account_key,
                                            table_name=table_name)
        self.logger.addHandler(log_handler)


    def get_logger(self):
        return self.logger
        

class table_handler(logging.Handler):
    def __init__(self, st_account_name, account_key, table_name):
        logging.Handler.__init__(self)
        #Connection string to the Table 'table_name' in Azure Storage Account 'account_name' with the authenticatoin key 'account_key'
        connection_string = (
            f"DefaultEndpointsProtocol=https;"
            f"AccountName={st_account_name};"
            f"AccountKey={account_key};"
            f"EndpointSuffix=core.windows.net"
        )

        self.service = TableServiceClient.from_connection_string(conn_str=connection_string)
        self.table_client = self.service.get_table_client(table_name=table_name)
        
        #Getting hostname of the system, it will be stored in a log entry
        self.hostname = gethostname()
        
        #PartitionKey is needed
        self.partition_key_formatter = logging.Formatter('%(asctime)s', '%Y%m%d%H%M')
        
        #Formatter for the row key
        self.row_key_formatter = logging.Formatter('%(created)f_%(process)d_%(thread)d_%(lineno)d', '%Y%m%d%H%M%S')


    def emit(self, record):
        #Creating an entry for the log
        record.hostname = self.hostname
        entity = {}
        entity['PartitionKey'] = self.partition_key_formatter.format(record)
        entity['RowKey'] = self.row_key_formatter.format(record)
        dict_log=record.__dict__
        entity['level'] = dict_log['levelname']
        entity['hostname'] = self.hostname
        entity['process'] = f"{dict_log['module']}.{dict_log['processName']}"
        entity['message'] = self.format(record)
        #Storing the entry in the table
        self.table_client.create_entity(entity)
