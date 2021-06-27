from sqlite3 import connect, OperationalError
from datetime import datetime


class AllNotes:
    def __init__(self):
        self.path = 'database.db'
        self.all_notes = []

    def select_data(self):
        try:
            with connect(self.path) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT `id`, `priority`, `text`, `category`, `creation_date`, `deadline`, `colour` FROM `notes`')
                result = cursor.fetchall()
                self.all_notes = result
                return result
        except OperationalError:
            with connect(self.path) as connection:
                cursor = connection.cursor()
                cursor.execute('CREATE TABLE `notes` ('
                               '`id` INTEGER PRIMARY KEY AUTOINCREMENT,'
                               '`priority` INTEGER,'
                               '`text` TEXT,'
                               '`category` TEXT,'
                               '`creation_date` TEXT,'
                               '`deadline` TEXT,'
                               '`colour` TEXT)')
                connection.commit()
                return self.select_data()

    def insert_data(self, priority: int, text: str, category: str, deadline: str, colour: str):
        creation_date = datetime.now().strftime('%Y.%m.%d')
        with connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO `notes` (`priority`, `text`, `category`, `creation_date`, `deadline`, `colour`)'
                'VALUES (?, ?, ?, ?, ?, ?)', (priority, text, category, creation_date, deadline, colour))
            connection.commit()
        self.select_data()

    def delete_data(self, primary_key: int):
        with connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM `notes` WHERE `id` = (?)', (primary_key,))
            connection.commit()
        self.select_data()
