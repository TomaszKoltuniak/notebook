from sqlite3 import connect, OperationalError
from datetime import datetime
from csv import writer


def log(module: str, list_of_data: list):
    data = [datetime.now(), module, list_of_data]
    with open('log', 'a', encoding='utf-8', newline='') as file:
        content = writer(file, delimiter=';')
        content.writerow(data)


class AllNotes:
    SORT_CRITERION = {
        'id': 0,
        'priority': 1,
        'text': 2,
        'category': 3,
        'creation_date': 4,
        'deadline': 5,
        'colour': 6,
    }

    def __init__(self):
        self.path = 'database.db'
        self.all_notes = []
        self.sort_reverse_status = True
        log('AllNotes.__init__', [f'DB_path={self.path}'])

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
            log('AllNotes.insert_data', [priority, text, category, creation_date, deadline, colour])
        self.select_data()

    def delete_data(self, primary_key: int):
        with connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM `notes` WHERE `id` = (?)', (primary_key,))
            connection.commit()
            log('AllNotes.delete_data', [primary_key])
        self.select_data()

    def sort_by(self, sort_criterion: str):
        self.all_notes = sorted(self.all_notes, key=lambda element: element[self.SORT_CRITERION[sort_criterion]],
                                reverse=self.sort_reverse_status)
        log('AllNotes.sort_by', [sort_criterion, f'Reverse={self.sort_reverse_status}'])
        self.sort_reverse_status = not self.sort_reverse_status
