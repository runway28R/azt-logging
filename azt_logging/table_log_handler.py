import logging
from socket import gethostname
from azure.data.tables import TableServiceClient
from azure.core.exceptions import ResourceExistsError


class table_logger:
    def __init__(self, st_account_name, account_key, table_name, log_level):
        #logger.setLevel(logging.DEBUG)
        #debug=10
        #info=20
        #warning=30
        #error=40
        #critical=50

        self.st_account_name = st_account_name
        self.account_key = account_key
        self.table_name = table_name
        self.connection_string = self.create_connection_string()

        self.create_table()
        table_client = self.create_table_client()
        self.logger = logging.getLogger(table_name)
        self.logger.setLevel(int(log_level))

        # Clear existing handlers to avoid duplicate logs
        if len(self.logger.handlers) > 0:
            self.logger.handlers.clear()

        log_handler = table_handler(table_client=table_client)
        self.logger.addHandler(log_handler)


    def create_connection_string(self):
        connection_string = (
            f"DefaultEndpointsProtocol=https;"
            f"AccountName={self.st_account_name};"
            f"AccountKey={self.account_key};"
            f"EndpointSuffix=core.windows.net"
        )
        return connection_string


    def create_table(self):
        try:
            service = TableServiceClient.from_connection_string(conn_str=self.connection_string)
            service.create_table(table_name=self.table_name)
        except ResourceExistsError:
            pass  # Table already exists → nothing to do
        except Exception as e:
            print(e)

    
    def create_table_client(self):
        service = TableServiceClient.from_connection_string(conn_str=self.connection_string)
        self.table_client = service.get_table_client(table_name=self.table_name)
        return self.table_client
    

    def get_logger(self):
        return self.logger
        

class table_handler(logging.Handler):
    def __init__(self, table_client):
        logging.Handler.__init__(self)
        self.table_client = table_client
        
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
