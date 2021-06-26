from tkinter import Tk, Label, Button, Entry, Frame, LabelFrame
from backend import AllNotes


class MainWindow:
    def __init__(self, root: Tk):
        self.root = root
        self.all_notes = AllNotes()

        # A Add new note bar
        self.a_new_note_frame = LabelFrame(self.root, text='Add new note')
        self.a_new_note_frame.grid(row=0, column=0)

        self.a_priority_frame = LabelFrame(self.a_new_note_frame, text='Priority')
        self.a_priority_frame.grid(row=0, column=0)
        self.a_priority_entry = Entry(self.a_priority_frame)
        self.a_priority_entry.pack()

        self.a_text_frame = LabelFrame(self.a_new_note_frame, text='Text')
        self.a_text_frame.grid(row=0, column=1)
        self.a_text_entry = Entry(self.a_text_frame, width=36)
        self.a_text_entry.pack()

        self.a_category_frame = LabelFrame(self.a_new_note_frame, text='Category')
        self.a_category_frame.grid(row=0, column=2)
        self.a_category_entry = Entry(self.a_category_frame)
        self.a_category_entry.pack()

        self.a_deadline_frame = LabelFrame(self.a_new_note_frame, text='Deadline')
        self.a_deadline_frame.grid(row=0, column=3)
        self.a_deadline_entry = Entry(self.a_deadline_frame)
        self.a_deadline_entry.insert(0, 'YYYY.MM.DD')
        self.a_deadline_entry.pack()

        self.a_colour_frame = LabelFrame(self.a_new_note_frame, text='Colour')
        self.a_colour_frame.grid(row=0, column=4)
        self.a_add_red = Button(self.a_colour_frame, text='Create', bg='red', fg='white')
        self.a_add_blue = Button(self.a_colour_frame, text='Create', bg='blue', fg='white')
        self.a_add_lime = Button(self.a_colour_frame, text='Create', bg='lime', fg='black')
        self.a_add_yellow = Button(self.a_colour_frame, text='Create', bg='yellow', fg='black')
        self.a_add_red.grid(row=0, column=0)
        self.a_add_blue.grid(row=0, column=1)
        self.a_add_lime.grid(row=0, column=2)
        self.a_add_yellow.grid(row=0, column=3)

        # S Sort notes bar
        self.s_sort_frame = LabelFrame(self.root, text='Sort by')
        self.s_sort_frame.grid(row=1, column=0)

        self.s_priority_button = Button(self.s_sort_frame, text='Priority', width=17)
        self.s_priority_button.grid(row=0, column=0)

        self.s_text_button = Button(self.s_sort_frame, text='Text', width=19)
        self.s_text_button.grid(row=0, column=1)

        self.s_category_button = Button(self.s_sort_frame, text='Category', width=18)
        self.s_category_button.grid(row=0, column=2)

        self.s_creation_date_button = Button(self.s_sort_frame, text='Creation date', width=17)
        self.s_creation_date_button.grid(row=0, column=3)

        self.s_deadline_button = Button(self.s_sort_frame, text='Deadline', width=17)
        self.s_deadline_button.grid(row=0, column=4)

        self.s_colour_button = Button(self.s_sort_frame, text='Colour', width=17)
        self.s_colour_button.grid(row=0, column=5)

        # All notes bar
        self.notes_frame = Frame(self.root)
        self.notes_frame.grid(row=2, column=0)
        temp_note = Note(self.notes_frame, 3, 22, 'Clean the room', 'Cleaning', '2021.06.20', '2021.06.29', 'red')
        temp_note.start()


class Note:
    COLOURS_BG_FG = {
        'red': 'white',
        'blue': 'white',
        'lime': 'black',
        'yellow': 'black'
    }

    def __init__(self, notes_frame: Frame, primary_key: int, priority: int, text: str, category: str,
                 creation_date: str, deadline: str, colour: str):
        self.notes_frame = notes_frame
        self.primary_key = primary_key
        self.priority = priority
        self.text = text
        self.category = category
        self.creation_date = creation_date
        self.deadline = deadline
        self.colour = colour

        self.my_frame = None
        self.priority_label = None
        self.text_label = None
        self.category_label = None
        self.creation_date_label = None
        self.deadline_label = None
        self.delete_button = None

    def start(self):
        self.my_frame = Frame(self.notes_frame, bg=self.COLOURS_BG_FG[self.colour])
        self.my_frame.pack()

        self.priority_label = Label(self.my_frame, text=self.priority, width=10)
        self.priority_label.grid(row=0, column=0)

        self.text_label = Label(self.my_frame, text=self.text, width=50)
        self.text_label.grid(row=0, column=1)

        self.category_label = Label(self.my_frame, text=self.category, width=10)
        self.category_label.grid(row=0, column=2)

        self.creation_date_label = Label(self.my_frame, text=self.creation_date, width=10)
        self.creation_date_label.grid(row=0, column=3)

        self.deadline_label = Label(self.my_frame, text=self.deadline, width=10)
        self.deadline_label.grid(row=0, column=4)

        self.delete_button = Button(self.my_frame, text='Delete', width=10)
        self.delete_button.grid(row=0, column=5)

    def end(self):
        self.my_frame.destroy()
