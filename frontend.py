from tkinter import Tk, Label, Button, Entry, Frame, LabelFrame
from backend import AllNotes


class MainWindow:
    def __init__(self, root: Tk):
        self.root = root
        self.all_notes = AllNotes()

        # All notes bar
        self.all_notes_frame = Frame(self.root)
        self.all_notes_frame.grid(row=2, column=0)

        # A Add new note bar
        self.a_new_note_frame = LabelFrame(self.root, text='Add new note')
        self.a_new_note_frame.grid(row=0, column=0)

        self.a_priority_frame = LabelFrame(self.a_new_note_frame, text='Priority')
        self.a_priority_frame.grid(row=0, column=0)
        self.a_priority_entry = Entry(self.a_priority_frame, width=8)
        self.a_priority_entry.pack()

        self.a_text_frame = LabelFrame(self.a_new_note_frame, text='Text')
        self.a_text_frame.grid(row=0, column=1)
        self.a_text_entry = Entry(self.a_text_frame, width=49)
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
        self.a_add_blue = Button(self.a_colour_frame, text='Create', bg='blue', fg='white',
                                 command=lambda: self.create_new_note('blue'))
        self.a_add_lime = Button(self.a_colour_frame, text='Create', bg='lime', fg='black',
                                 command=lambda: self.create_new_note('lime'))
        self.a_add_red = Button(self.a_colour_frame, text='Create', bg='red', fg='white',
                                command=lambda: self.create_new_note('red'))
        self.a_add_yellow = Button(self.a_colour_frame, text='Create', bg='yellow', fg='black',
                                   command=lambda: self.create_new_note('yellow'))
        self.a_add_blue.grid(row=0, column=0)
        self.a_add_lime.grid(row=0, column=1)
        self.a_add_red.grid(row=0, column=2)
        self.a_add_yellow.grid(row=0, column=3)

        # S Sort notes bar
        self.s_sort_frame = LabelFrame(self.root, text='Sort by')
        self.s_sort_frame.grid(row=1, column=0)

        self.s_priority_button = Button(self.s_sort_frame, text='Priority', width=5,
                                        command=lambda: self.sort_by('priority'))
        self.s_priority_button.grid(row=0, column=0)

        self.s_text_button = Button(self.s_sort_frame, text='Text', width=55, command=lambda: self.sort_by('text'))
        self.s_text_button.grid(row=0, column=1)

        self.s_category_button = Button(self.s_sort_frame, text='Category', width=20,
                                        command=lambda: self.sort_by('category'))
        self.s_category_button.grid(row=0, column=2)

        self.s_creation_date_button = Button(self.s_sort_frame, text='Creation date', width=12,
                                             command=lambda: self.sort_by('creation_date'))
        self.s_creation_date_button.grid(row=0, column=3)

        self.s_deadline_button = Button(self.s_sort_frame, text='Deadline', width=8,
                                        command=lambda: self.sort_by('deadline'))
        self.s_deadline_button.grid(row=0, column=4)

        self.s_colour_button = Button(self.s_sort_frame, text='Colour', width=5,
                                      command=lambda: self.sort_by('colour'))
        self.s_colour_button.grid(row=0, column=5)

        self.print_all_notes()

    def print_all_notes(self, sort: bool = False):
        self.all_notes_frame = Frame(self.root)
        self.all_notes_frame.grid(row=2, column=0)
        if sort is False:
            for primary_key, priority, text, category, creation_date, deadline, colour in self.all_notes.select_data():
                Note(self.all_notes, self.all_notes_frame, priority, text, category, deadline, colour, primary_key,
                     creation_date)
        elif sort is True:
            for primary_key, priority, text, category, creation_date, deadline, colour in self.all_notes.all_notes:
                Note(self.all_notes, self.all_notes_frame, priority, text, category, deadline, colour, primary_key,
                     creation_date)

    def deprint_all_notes(self):
        self.all_notes_frame.destroy()

    def sort_by(self, sort_criterion: str):
        self.all_notes.sort_by(sort_criterion)
        self.deprint_all_notes()
        self.print_all_notes(True)

    def create_new_note(self, colour: str):
        self.all_notes.insert_data(self.a_priority_entry.get(), self.a_text_entry.get(), self.a_category_entry.get(),
                                   self.a_deadline_entry.get(), colour)
        self.deprint_all_notes()
        self.print_all_notes()


class Note:
    COLOURS_BG_FG = {
        'red': 'white',
        'blue': 'white',
        'lime': 'black',
        'yellow': 'black'
    }

    def __init__(self, all_notes: AllNotes, all_notes_frame: Frame, priority: int, text: str, category: str,
                 deadline: str, colour: str, primary_key: int = None, creation_date: str = None):
        self.all_notes = all_notes
        self.all_notes_frame = all_notes_frame
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

        self.start()

    def start(self):
        self.my_frame = Frame(self.all_notes_frame)
        self.my_frame.pack()

        self.priority_label = Label(self.my_frame, text=self.priority, width=5, bg=self.colour,
                                    fg=self.COLOURS_BG_FG[self.colour])
        self.priority_label.grid(row=0, column=0)

        self.text_label = Label(self.my_frame, text=self.text, width=58, bg=self.colour,
                                fg=self.COLOURS_BG_FG[self.colour], anchor='w')
        self.text_label.grid(row=0, column=1)

        self.category_label = Label(self.my_frame, text=self.category, width=20, bg=self.colour,
                                    fg=self.COLOURS_BG_FG[self.colour])
        self.category_label.grid(row=0, column=2)

        self.creation_date_label = Label(self.my_frame, text=self.creation_date, width=10, bg=self.colour,
                                         fg=self.COLOURS_BG_FG[self.colour])
        self.creation_date_label.grid(row=0, column=3)

        self.deadline_label = Label(self.my_frame, text=self.deadline, width=10, bg=self.colour,
                                    fg=self.COLOURS_BG_FG[self.colour])
        self.deadline_label.grid(row=0, column=4)

        self.delete_button = Button(self.my_frame, text='Delete', width=5, bg=self.colour,
                                    fg=self.COLOURS_BG_FG[self.colour], command=lambda: self.delete())
        self.delete_button.grid(row=0, column=5)

    def delete(self):
        self.my_frame.destroy()
        self.all_notes.delete_data(self.primary_key)
