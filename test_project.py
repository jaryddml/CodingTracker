import pytest
from unittest.mock import patch
from project import Tracker
import sqlite3

@pytest.fixture
def mock_db():
    with patch('project.create_connection') as mock_create:
        conn = sqlite3.connect(':memory:') 
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE tasks (
                name TEXT,
                extension TEXT,
                directory TEXT,
                duration REAL,
                UNIQUE(name, extension, directory)
            )
            """
        )
        conn.commit()
        mock_create.return_value = conn
        yield conn
        conn.close()


def test_split_window_name():
    tracker = Tracker()
    input_str = "file.py - /path/to/file - Visual Studio Code"
    expected = ("file.py", ".py", "/path/to/file")
    assert tracker.split_window_name(input_str) == expected


def test_insert_update_data(mock_db):
    tracker = Tracker()
    # First insert
    tracker.insert_update_data("file.py", ".py", "/path/to/file", 30)
    # Now update
    tracker.insert_update_data("file.py", ".py", "/path/to/file", 70)

    cur = mock_db.cursor()
    cur.execute("SELECT duration FROM tasks WHERE name = 'file.py' AND extension = '.py' AND directory = '/path/to/file'")
    result = cur.fetchone()
    assert result[0] == 100 

