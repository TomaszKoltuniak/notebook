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
                    'SELECT `priority`, `text`, `category`, `creation_date`, `deadline`, `colour` FROM notes')
                result = cursor.fetchall()
                self.all_notes = result
                return result
        except OperationalError:
            with connect(self.path) as connection:
                cursor = connection.cursor()
                cursor.execute('CREATE TABLE `notes` ('
                               '`id` INTEGER PRIMARY KEY AUTOINCREMENT,'
                               '`priority` TEXT,'
                               '`text` TEXT,'
                               '`category` TEXT,'
                               '`creation_date` DATETIME,'
                               '`deadline` DATETIME,'
                               '`colour` TEXT)')
                return self.select_data()

    def insert_data(self, priority: int, text: str, category: str, deadline: str, colour: str):
        creation_date = datetime.now().strftime('%Y.%m.%d %H:%M')
        with connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO `notes` (`priority`, `text`, `category`, `creation_date`, `deadline`, `colour`)'
                'VALUES (?, ?, ?, ?, ?, ?)', (priority, text, category, creation_date, deadline, colour))
            connection.commit()

# 'YYYY.MM.DD HH:MM'
# CREATE TABLE `notes` (
#   `id` int(11) NOT NULL,
#   `priority` int(11) NOT NULL,
#   `text` text COLLATE utf8_polish_ci NOT NULL,
#   `category` text COLLATE utf8_polish_ci NOT NULL,
#   `creation_date` datetime NOT NULL,
#   `deadline` datetime NOT NULL,
#   `colour` text COLLATE utf8_polish_ci NOT NULL
# )
