from datetime import datetime
import logging
from table_log_handler import table_log_handler

class Log:
    def __init__(st_account_name, account_key, log_table, log_level):
        #logger.setLevel(logging.DEBUG)
        #notset=0
        #trace=5\does not exist!
        #debug=10
        #info=20
        #warning=30
        #error=40
        #critical=50
        
        logger = logging.getLogger(log_table)
        logger.setLevel(int(log_level))
        if len(logger.handlers)>0:
            logger.handlers.clear()
        log_handler = table_log_handler(st_account_name=st_account_name,
                                            account_key=account_key,
                                            table_name=log_table)
        logger.addHandler(log_handler)

        return logger
