from sqlite3 import connect


class AllNotes:
    def __init__(self):
        self.path = 'database.db'
        self.all_notes = []

    def import_data(self):
        with connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT `priority`, `text`, `category`, `creation_date`, `deadline`, `colour`')
# CREATE TABLE `notes` (
#   `id` int(11) NOT NULL,
#   `priority` int(11) NOT NULL,
#   `text` text COLLATE utf8_polish_ci NOT NULL,
#   `category` text COLLATE utf8_polish_ci NOT NULL,
#   `creation_date` datetime NOT NULL,
#   `deadline` datetime NOT NULL,
#   `colour` text COLLATE utf8_polish_ci NOT NULL
# )
