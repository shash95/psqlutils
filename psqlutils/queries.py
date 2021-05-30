# This module contains all the queries required in the project

# Queries for database level operations
GET_SCHEMAS_QUERY = "SELECT SCHEMA_NAME FROM {information_schema}.{schemata}"

# Queries for schema level operations

GET_TABLES_QUERY = "SELECT TABLE_NAME FROM {information_schema}.{tables} where table_schema='{schema_name}'"

# Queries for table level operations

GET_COLUMNS_QUERY = "SELECT column_name, ordinal_position, data_type from {information_schema}.{columns} where" \
                    " table_schema='{schema_name}' and table_name='{table_name}'"
