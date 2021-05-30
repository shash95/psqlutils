import psqlutils

connection_config = {
    "database_name": "postgres",
    "port": 5432,
    "username": "postgres",
    "password": "admin",
    "host": "localhost"
}
schema_name = "utils_test1"
table_name = "t1"

GET_SCHEMAS = 0
GET_TABLES = 0
GET_COLUMNS = 1

if GET_SCHEMAS:
    schema_list = psqlutils.PsqlUtils().get_schemas(
        connection_config=connection_config, include_default_schemas=False, log_level="debug"
    )
    print(schema_list)

if GET_TABLES:
    table_list = psqlutils.PsqlUtils().get_tables(
        connection_config=connection_config, log_level="debug", schema_name=schema_name)
    print(table_list)

if GET_COLUMNS:
    column_list = psqlutils.PsqlUtils().get_columns(
        connection_config=connection_config, log_level="debug", schema_name=schema_name, table_name=table_name
    )
    print(column_list)
