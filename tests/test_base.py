import sqlite3
import os
from pyliteway.migrator import PyLiteWay
from pyliteway.migrator import get_migrations

def test_create_history_table_if_does_not_exist():
    conn = sqlite3.connect(":memory:")
    pyLiteWay = PyLiteWay(conn, "tests/db/migrations1")
    pyLiteWay._init_history_table()

    cursor = conn.execute("SELECT * from sqlite_master WHERE type='table' AND name='pyliteway_schema_history';")
    assert cursor.fetchone() is not None 

def test_get_migrations():
    path_to_test_sql = os.path.join(os.path.abspath('.'), "tests/db/migrations1")
    migrations = get_migrations(path_to_test_sql)
    assert len(migrations) == 1
    assert "V0001__test_example.sql" in migrations
