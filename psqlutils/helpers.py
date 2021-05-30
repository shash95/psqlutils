# Module to store some common helper methods
from .execute import execute
from .logging import get_logger

MODULE_NAME = "helpers"


def get_value_list(query, connection_config, log_level):
    """
    :param query:
        Type:string
        Purpose: The query to be executed. Multiple queries are not supported.
    :param connection_config:
        Type: dict
        Purpose: Connection details required to connect to the database
        Details:
        Following is the dict structure expected by the module
        {
            "host": "string",
            "port": "integer",
            "db_name": "string",
            "username": "string",
            "password": "string"
        }
        key host: Hostname for the database on which query has to be executed
        key port: Port number on which the database is running
        key db_name: Database name on which the query has to be executed
        key username: Username to connect to the database
        key password: Password to connect to the database
    :param log_level:
        Type: string
        Purpose: Sets the logging level
    """
    logger = get_logger(MODULE_NAME, log_level)
    logger.info("Starting method get_value_list()")
    query_response = execute(
        query=query, connection_config=connection_config, log_level=log_level, fetch_raw_response=True
    )
    value_list = []
    for row in query_response:
        value_list.append(row[0])
    return value_list
