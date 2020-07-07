import tkinter as tk
import random

# Funtion
def roll_dice():
    rng = random.Random()
    value = rng.randint(1,6)
    result["text"] = "{0}".format(value)

# Apperance

window = tk.Tk()

window.rowconfigure([0,1], minsize=50, weight=1)
window.columnconfigure([0], minsize=50, weight=1)

button = tk.Button(master=window, text="Roll", command=roll_dice)
button.grid(row=0, column=0)


result = tk.Label(master=window, text="")
result.grid(row=1, column=0)






window.mainloop()