import tkinter as tk

# Backbone
def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = "{0}".format(value + 1)

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = "{0}".format(value - 1)

# Apperance

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0,1,2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")




window.mainloop()