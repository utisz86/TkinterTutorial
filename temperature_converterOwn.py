import tkinter as tk

# Apperance
window = tk.Tk()

window.rowconfigure([0], minsize=50, weight=1)
window.columnconfigure([0,1,2,3,4], weight=1)

ent_temperature = tk.Entry()
ent_temperature.grid(row=0, column=0)

ent_temperatureLabel = tk.Label(text="\N{DEGREE FAHRENHEIT}")
ent_temperatureLabel.grid(row=0, column=1)

btn_convert = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}")
btn_convert.grid(row=0, column=2)

lbl_resultLab1 = tk.Label(text="")
lbl_resultLab1.grid(row=0, column=3)

lbl_resultLab2 = tk.Label(text="\N{DEGREE CELSIUS}")
lbl_resultLab2.grid(row=0, column=4)



window.mainloop()