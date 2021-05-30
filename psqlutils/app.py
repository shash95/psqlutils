from .execute import execute
from .helpers import get_value_list
from .logging import get_logger
from .queries import *
from .constants import *


# MODULE_NAME = "app"

class PsqlUtils:

    def __init__(self):
        self.module_name = "app"

    def get_schemas(self, connection_config, include_default_schemas, log_level=DEFAULT_LOGGER_LEVEL):
        """
        This method gets a list of schemas present in the given database
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
        :param include_default_schemas:
            Type: boolean
            Purpose: Indicates whether the default schemas should be returned or not
        :param log_level:
            Type: string
            Purpose: Sets the logging level
        :return:
        """
        logger = get_logger(self.module_name, log_level)
        logger.info("Starting method get_schemas()")
        get_schemas_query = GET_SCHEMAS_QUERY.format(
            information_schema=INFORMATION_SCHEMA_KEY, schemata=SCHEMATA_KEY, connection_config=connection_config,
            log_level=log_level
        )
        logger.debug("Executing query - {}".format(get_schemas_query))
        schema_list = get_value_list(query=get_schemas_query, connection_config=connection_config, log_level=log_level)
        # remove default schemas if include_default_schemas=False
        if not include_default_schemas:
            for schema in DEFAULT_SCHEMA_LIST:
                if schema in schema_list:
                    schema_list.remove(schema)
        return schema_list

    def get_tables(self, connection_config, schema_name, log_level=DEFAULT_LOGGER_LEVEL):
        """
        This method gets a list of tables present in a given schema
        :param connection_config:
        :param schema_name
        :param log_level:
        :return:
        """
        logger = get_logger(self.module_name, log_level)
        logger.info("Starting method get_tables()")
        get_tables_query = GET_TABLES_QUERY.format(
            information_schema=INFORMATION_SCHEMA_KEY, tables=TABLES_KEY, schema_name=schema_name
        )
        logger.debug("Executing query - {}".format(get_tables_query))
        table_list = get_value_list(query=get_tables_query, connection_config=connection_config, log_level=log_level)
        return table_list

    def get_columns(self, connection_config, schema_name, table_name, log_level=DEFAULT_LOGGER_LEVEL):
        """

        :param connection_config:
        :param schema_name:
        :param table_name:
        :param log_level:
        :return:
        """
        logger = get_logger(self.module_name, log_level)
        logger.info("Starting method get_columns")
        get_columns_query = GET_COLUMNS_QUERY.format(
            information_schema=INFORMATION_SCHEMA_KEY, columns=COLUMNS_KEY, schema_name=schema_name,
            table_name=table_name)
        logger.debug("Executing query - {}".format(get_columns_query))
        column_list = execute(
            query=get_columns_query, connection_config=connection_config, fetch_raw_response=False, log_level=log_level)
        return column_list
