# shadow coded Bro Code (youtube channel)
from tkinter import *
from time import *

# define clock update function
def update_clock():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%d %B %Y")
    date_label.config(text=date_string)

    window.after(1000, update_clock)

# window GUI labels
window = Tk()
window.title("Clock")

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Arial", 25))
day_label.pack()

date_label = Label(window, font=("Arial", 25))
date_label.pack()

# Update the clock
update_clock()
window.mainloop()