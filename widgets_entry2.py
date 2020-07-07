import tkinter as tk

window = tk.Tk()

# create a Label and an Entry widget
label = tk.Label(text="Name")
entry = tk.Entry()

# visible
label.pack()
entry.pack()

entry.insert(0,"mi?")
name = entry.get()
print(name)

window.mainloop()