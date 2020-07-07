import tkinter as tk

window = tk.Tk()

# Generate - label
greeting = tk.Label(text="Hello, Tkinter", foreground = "white", background = "black", width=10, height=10)

# Add to window
greeting.pack()

window.mainloop()