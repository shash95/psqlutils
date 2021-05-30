import psycopg2
from copy import deepcopy

from .logging import get_logger
from .constants import *


MODULE_NAME = "execute"


def execute(query, connection_config, fetch_raw_response, log_level):
    """
    Function to execute a query on PostgreSQL database
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
    :param fetch_raw_response:
        Type: boolean
        Purpose: Set the value to true if direct response from the cursor is required
            If set to false, response will be restructured as list of dictionaries
    :return:
        Type: list
        Contains a list of dict items if query runs successfully, else exception is raised
    """
    logger = get_logger(MODULE_NAME, log_level)
    logger.debug("Starting method execute()")
    connection = _get_connection(connection_config, log_level)
    cursor = connection.cursor()
    cursor.execute(query)
    logger.debug("Query executed successfully")
    rows = cursor.fetchall()
    _close_connection(connection, log_level)
    if len(rows) == 0:
        logger.debug("No rows returned by the query")
    if fetch_raw_response:
        return rows
    logger.debug("Formatting response to list of dicts")
    result_list = []
    for row in rows:
        row_dict = deepcopy({})
        for index, column_element in enumerate(cursor.description):
            row_dict[column_element.name] = row[index]
        result_list.append(row_dict)


    return result_list


def _get_connection(connection_config, log_level):
    """
    Creates a psycopg2 connection to the PostgreSQL database
    param connection_config:
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
    :return:
        Type: connection
        Returns the connection to the PostgreSQL database
    """
    logger = get_logger(MODULE_NAME, log_level)
    logger.info("Starting method _get_connection")
    _validate_inputs(connection_config, log_level)
    logger.debug("Connection config is valid")
    host = connection_config[HOST_KEY]
    port = connection_config[PORT_KEY]
    username = connection_config[USERNAME_KEY]
    password = connection_config[PASSWORD_KEY]
    database_name = connection_config[DATABASE_NAME_KEY]

    try:
        conn = psycopg2.connect(database=database_name, user=username, password=password, host=host, port=port)
        logger.debug("Database connection established successfully")
    except:
        raise Exception("Failed to establish connection to the database")

    return conn
    pass


def _validate_inputs(connection_config, log_level):
    """
    Validates the connection config to check if all required keys are provided
    :param connection_config:
        Type: dict
        Purpose: The connection config which should be used to establish connection to the PostgreSQL database
    :param log_level:
        Type: string
        Purpose: Sets the logging level
    :return:
        Type: boolean
        Returns the boolean value which indicates whether the connection config is valid or not
    """
    logger = get_logger(MODULE_NAME, log_level)
    logger.info("Starting method _validate_inputs()")

    missing_keys = []
    for key in CONNECTION_CONFIG_MANDATORY_KEYS:
        if key not in connection_config.keys():
            missing_keys.append(key)

    if len(missing_keys) != 0:
        raise Exception("Mandatory keys missing in input - {}".format(",".join(missing_keys)))

    logger.info("Completed method _validate_inputs()")
    return True


def _close_connection(connection, log_level):
    logger = get_logger(MODULE_NAME, log_level)
    logger.info("Starting method _close_connection()")
    logger.debug("Closing the connection")
    connection.close()
    logger.debug("Connection closed")
    logger.info("Completed method _close_connection()")