import tkinter as tk

window = tk.Tk()

# Generate - button
button = tk.Button(text="Click me!", width=25, height=5, bg="blue", fg="yellow")

# Add to window
button.pack()

window.mainloop()