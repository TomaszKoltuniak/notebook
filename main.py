from frontend import MainWindow
from tkinter import Tk


class Application:
    @staticmethod
    def main():
        root = Tk()
        root.title('Notebook')
        root.geometry('800x900')
        MainWindow(root)
        root.mainloop()


if __name__ == '__main__':
    app = Application()
    app.main()
