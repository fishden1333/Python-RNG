import sys
import random

# Check the Python version
if sys.version_info[0] == 3:
    from tkinter import *
else:
    from Tkinter import *

# Generate a random integer in the range upper to lower
def start_rng():
    lower = int(e1.get())
    upper = int(e2.get())
    num = random.randint(lower, upper)
    w3 = Label(root,
               text = num,
               pady = 5,
               padx = 10,
               justify = RIGHT).grid(row = 2, column = 1)
    s = "Upper: " + repr(lower) + ", Lower: " + repr(upper) + "\n" + "Random: " + repr(num) + "\n"
    print(s)

# Main window
root = Tk()
root.title("RNG Generator")

# Labels
w1 = Label(root,
           text = "Lower bound",
           pady = 10,
           padx = 10).grid(row = 0)
w2 = Label(root,
           text = "Upper bound",
           pady = 10,
           padx = 10).grid(row = 1)

# Entries
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

# Start button
b = Button(root,
            text = "Start",
            pady = 10,
            padx = 10,
            command = start_rng).grid(row = 2)

root.mainloop()
