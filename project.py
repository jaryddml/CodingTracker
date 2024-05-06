import ewmh
import time
from ewmh import EWMH
import sqlite3
import threading
from pathlib import Path


#  This only works on linux. You need to install the python-xlib package.
#  This only works for Visual Studio Code
#  Editors like nvim do not change window name when you change files so it will not work for them.


class Tracker:
    def __init__(self):
        self.ewmh = EWMH()
        self.window = None
        self.active_window_name = None
        self.start_time = None
        self.duration = 0
        self.file_name = None
        self.file_extension = None
        self.directory = None

    def get_active_window_name(self):
        #  Do not judge the ugly nested 'if' statments. 
        last_window = None
        while True:
            window = self.ewmh.getActiveWindow()
            if window:
                window_name = self.ewmh.getWmName(window).decode("utf-8")
                if "Visual Studio Code" in window_name:
                    if window_name != last_window:
                        self.process_active_window(last_window)
                        last_window = window_name
                        self.start_time = time.time()
                        parsed_name = self.split_window_name(window_name)
                        if parsed_name:
                            self.file_name, self.file_extension, self.directory = (
                                parsed_name
                            )

                elif last_window:
                    self.process_active_window(last_window)
                    last_window = None
            time.sleep(1)

    def process_active_window(self, last_window):
        if last_window and self.start_time:
            self.end_time = time.time()
            self.duration = self.end_time - self.start_time
            self.insert_update_data(
                self.file_name, self.file_extension, self.directory, self.duration
            )
            print(
                f"Updated Data: {self.file_name, self.file_extension, self.directory} with duration {self.duration}"
            )

    def split_window_name(self, window_name):
        data = window_name.split("-")
        if len(data) == 3:
            file_name = data[0].strip().replace("●", "").strip()
            directory = data[1].strip()
            file_extension = Path(file_name).suffix
            return file_name, file_extension, directory
        return None

    def insert_update_data(self, file_name, file_extension, directory, duration):
        with create_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                """SELECT duration FROM tasks WHERE name = ? AND extension = ? AND directory = ?""",
                (file_name, file_extension, directory),
            )
            result = cur.fetchone()
            if result:
                new_duration = result[0] + duration
                cur.execute(
                    """UPDATE tasks SET duration = ? WHERE name = ? AND extension = ? AND directory = ?""",
                    (new_duration, file_name, file_extension, directory),
                )
            else:
                cur.execute(
                    """INSERT INTO tasks (name, extension, directory, duration) VALUES (?, ?, ?, ?)""",
                    (file_name, file_extension, directory, duration),
                )
            conn.commit()


def main():
    create_table()
    construct_tracker_threaded()


def construct_tracker_threaded():

    tracker = Tracker()
    thread = threading.Thread(target=tracker.get_active_window_name)
    thread.start()


def create_connection():
    return sqlite3.connect("tracker.db")


def create_table():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS tasks (
        name TEXT,
        extension TEXT,
        directory TEXT,
        duration REAL,
        UNIQUE(name, extension, directory)
    )
    """
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
