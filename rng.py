import sys
import random

# Check the Python version
if sys.version_info[0] == 3:
    from tkinter import *
else:
    from Tkinter import *

# Generate a random integer in the range upper to lower
def start_rng():
    try:
        lower = int(e1.get())
    except ValueError:
        print("Error: Lower bound is not a valid integer")
        i = Label(root,
                  text = "Fill in a valid integer.",
                  fg = "red",
                  width = 20,
                  pady = 7,
                  padx = 10).grid(row = 0, columnspan = 2)
    try:
        upper = int(e2.get())
    except ValueError:
        print("Error: Upper bound is not a valid integer")
        i = Label(root,
                  text = "Fill in a valid integer.",
                  fg = "red",
                  width = 20,
                  pady = 7,
                  padx = 10).grid(row = 0, columnspan = 2)

    num = random.randint(lower, upper)
    w3 = Label(root,
               text = num,
               fg = "red",
               font = "Helvetica 25 bold",
               pady = 5,
               padx = 10,
               justify = RIGHT).grid(row = 3, column = 1)
    i = Label(root,
              text = "Fill in integer in the two entries.",
              pady = 7,
              padx = 10).grid(row = 0, columnspan = 2)
    s = "Upper: " + repr(lower) + ", Lower: " + repr(upper) + "\n" + "Random: " + repr(num) + "\n"
    print(s)

# Main window
root = Tk()
root.title("RNG")
root.geometry("240x170")

# Instructions
i = Label(root,
          text = "Fill in integer in the two entries.",
          pady = 7,
          padx = 10).grid(row = 0, columnspan = 2)

# Labels
w1 = Label(root,
           text = "Lower bound",
           pady = 10,
           padx = 10).grid(row = 1)
w2 = Label(root,
           text = "Upper bound",
           pady = 10,
           padx = 10).grid(row = 2)

# Entries
e1 = Entry(root,
           width = 12)
e2 = Entry(root,
           width = 12)
e1.grid(row = 1, column = 1)
e2.grid(row = 2, column = 1)

# Start button
b = Button(root,
            text = "Start",
            width = 5,
            borderwidth = 5,
            pady = 10,
            padx = 10,
            command = start_rng).grid(row = 3)

root.mainloop()
