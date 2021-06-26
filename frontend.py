from tkinter import Tk, Label, Button, Entry, Frame, LabelFrame


class MainWindow:
    def __init__(self, root: Tk):
        self.root = root
        self.new_note_frame = LabelFrame(self.root, text='Add new note', padx=3, pady=3)
        self.new_note_frame.grid(row=0, column=0)

        self.priority_frame = LabelFrame(self.new_note_frame, text='Priority', padx=3, pady=3)
        self.priority_frame.grid(row=0, column=0)
        self.priority_entry = Entry(self.priority_frame)
        self.priority_entry.pack()

        self.text_frame = LabelFrame(self.new_note_frame, text='Text', padx=3, pady=3)
        self.text_frame.grid(row=0, column=1)
        self.text_entry = Entry(self.text_frame, width=30)
        self.text_entry.pack()

        self.category_frame = LabelFrame(self.new_note_frame, text='Category', padx=3, pady=3)
        self.category_frame.grid(row=0, column=2)
        self.category_entry = Entry(self.category_frame)
        self.category_entry.pack()

        self.deadline_frame = LabelFrame(self.new_note_frame, text='Deadline', padx=3, pady=3)
        self.deadline_frame.grid(row=0, column=3)
        self.deadline_entry = Entry(self.deadline_frame)
        self.deadline_entry.insert(0, 'YYYY.MM.DD HH:MM')
        self.deadline_entry.pack()

        self.colour_frame = LabelFrame(self.new_note_frame, text='Colour', padx=3, pady=3)
        self.colour_frame.grid(row=0, column=4)
        self.add_red = Button(self.colour_frame, text='Dodaj', bg='red', fg='white')
        self.add_blue = Button(self.colour_frame, text='Dodaj', bg='blue', fg='white')
        self.add_lime = Button(self.colour_frame, text='Dodaj', bg='lime', fg='black')
        self.add_yellow = Button(self.colour_frame, text='Dodaj', bg='yellow', fg='black')
        self.add_red.grid(row=0, column=0)
        self.add_blue.grid(row=0, column=1)
        self.add_lime.grid(row=0, column=2)
        self.add_yellow.grid(row=0, column=3)

        self.sort_by_bar = LabelFrame(self.root, text='Sort by')
        self.sort_by_bar.grid(row=1, column=0)
        self.all_notes_bar = LabelFrame(self.root, text='All notes')
        self.all_notes_bar.grid(row=2, column=0)
