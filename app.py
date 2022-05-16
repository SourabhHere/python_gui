"""
purpose: to build a sample gui app using python capable of taking input and acting upon it.
         (no external library used)
author: Sourabh Katoch (16-05-2022)
"""


from tkinter import Tk, StringVar
from tkinter import ttk


def print_data():
    """function to print data input from app onto the console"""
    print(contents.get())


root = Tk()
main_frame = ttk.Frame(root, padding=10)
main_frame.grid()
root.configure(width=900, height=5)
contents = StringVar()

ttk.Label(main_frame, text='Enter Input', padding=10).grid(column=0, row=1)
ttk.Label(main_frame, text='A sample application which can interact with user and \
take input.', padding=10).grid(row=0, columnspan=4)

ttk.Entry(main_frame, textvariable=contents).grid(column=1, row=1)
ttk.Button(main_frame, text='print on terminal',
           command=print_data, padding=5).grid(column=2, row=1)
ttk.Button(main_frame, text='Quit', command=root.destroy,
           padding=5).grid(column=3, row=1)

root.mainloop()
