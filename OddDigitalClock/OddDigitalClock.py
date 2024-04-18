from tkinter import *
from tkinter import ttk
import time
import random

# create the main window as root
root = Tk()

# changing color of clock dictionary
my_dict = {
    1: ("black", "yellow"),
    2: ("blue", "red"),
    3: ("purple", "black"),
    4: ("yellow", "black"),
    5: ("green", "gray"),
    6: ("orange", "black"),
    7: ("pink", "blue"),
    8: ("brown", "yellow"),
    9: ("gray", "white"),
    10: ("white", "red"),
}


# get date and time by this function
def show_label_time():
    random_number = random.randint(1, 10)
    my_label2.config(text=time.strftime("%H:%M:%S-%Y:%m:%d"),
                     bg=my_dict[random_number][0], fg=my_dict[random_number][1])
    # this function repeats every 1000 ms while the window is running
    my_label2.after(1000, show_label_time)


# config the window
root.title('Odd Digital Clock')
root.geometry('750x450')

my_label = Label(root, text='hello my friend,\n welcome to my digital clock!', bg='black', fg='white',
                 font=('Arial', 31))
my_label2 = Label(root, text='H', bg='blue', fg='yellow', font=('arial', 52))
my_label3 = Label(root, text='Changing Color Option', bg='white', font=('arial', 25))
show_label_time()
my_label.pack()
my_label2.pack()
my_label3.pack()

root.mainloop()
