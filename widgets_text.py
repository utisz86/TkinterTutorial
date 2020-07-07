import tkinter as tk

window = tk.Tk()
text_box = tk.Text()
text_box.pack()

text = text_box.get("1.0")
print(text)

text_box.get("1.0", tk.END)

text_box.insert("1.0", "Hello")

window.mainloop()
