import os
import sqlite3

# returns the list of sql migration located in the sql_path
def get_migrations(migrations_dir: str) -> list:
    return [f for f in os.listdir(migrations_dir) if f.endswith('.sql')]

def apply_migration(sql_path: str, sql_file_name: str) -> bool:
    return True;

# returns the version of migration from the file

def extract_version(filename: str) -> str:
    # Split the filename on '__'
    parts = filename.split('__')
    # The code is the second part of the first split, so we split again on 'V'
    code = parts[0].split('V')[1]
    if code is None or len(code) == 0 or not code.isdigit():
        raise ValueError(f"Invalid migration file name: {filename}")
    return code


class PyLiteWay:
    def __init__(self, connection: sqlite3.Connection, migrations_dir: str, table: str = "pyliteway_schema_history"):
        if connection is None:
            raise ValueError("Connection is not specified")
        if migrations_dir is None:
            raise ValueError("SQL Path is not specified")
        self.table = table
        self.connection = connection
        self.sql_path = migrations_dir

    def get_db_path(self):
        return self.path
    
    def get_slq_path(self):
        return self.sql_path
    
    # Migrates the database to the latest version
    def migrate(self) -> bool:
        self._init_history_table()
        migrations = get_migrations(self.sql_path)
        # sort the migrations alphabetically
        migrations.sort()
        #TODO impement the migration


    def _apply_migration(self, sql_file_name: str) -> bool:
        return True

    # creates history table if doesn't exsit
    def _init_history_table (self) -> None:
        cursor = self.connection.execute(f"SELECT * from sqlite_master WHERE type='table' AND name='{self.table}';")
        # if the table exists, return
        if cursor.fetchone():
            return True
        
        create_table_query = f"""
            CREATE TABLE {self.table} (
                version TEXT PRIMARY KEY,
                script TEXT NOT NULL,
                installed_on TIMESTAMP NOT NULL
            );
        """
        # create the table
        self.connection.execute(create_table_query)
        self.connection.commit()
    
    