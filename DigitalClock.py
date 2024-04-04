from tkinter import *
from tkinter import ttk
import time

root = Tk()


def show_label_time():
    Hour = time.strftime("%H")
    Min = time.strftime("%M")
    Seconds = time.strftime("%S")
    my_label2.config(text=f"{Hour}:{Min}:{Seconds}")
    my_label2.after(1000, show_label_time)


root.title('Digital Clock!')
root.geometry('750x450')

my_label = Label(root, text='hello my friend,\n welcome to my digital clock!', bg='black', fg='white',
                 font=('Arial', 31))
my_label2 = Label(root, text='H', bg='blue', fg='yellow', font=('arial', 52))
show_label_time()
# my_label.pack(fill=BOTH)
# my_label2.pack(fill=BOTH, expand=True)
my_label.pack()
my_label2.pack(expand=True, fill=BOTH)
button = Button(root, text='Click Me!')

root.mainloop()
