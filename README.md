# psqlutils
This module contains methods to quickly get important details about your PostgreSQL database.

## Features
* Get list of all schemas present in the database
* Get list of all tables in any given schema
* Get column description for any given table


## Getting Started
* Simply clone the git repository in your working directory to get started
* Start writing your code in parallel to the psqlutils folder

## Import

```
from psqlutils import psqlutils
```

## Usage

```
connection_config = {
    "database_name": "postgres",
    "port": 5432,
    "username": "postgres",
    "password": "",
    "host": "localhost"
}

include_default_schemas = False

schema_list = psqlutils.get_schemas(connection_config, include_default_schemas)

print(schema_list)
```

