import tkinter as tk

from screeninfo import get_monitors
from tkinter import ttk

checkbox_vars = []
checkboxes = []

values = [
 "dolnośląskie",
 "kujawsko-pomorskie",
 "lubelskie",
 "lubuskie",
 "łódzkie",
 "małopolskie",
 "mazowieckie",
 "opolskie",
 "podkarpackie",
 "podlaskie",
 "pomorskie",
 "śląskie",
 "świętokrzyskie",
 "warmińsko-mazurskie",
 "wielkopolskie",
 "zachodniopomorskie"
]

def change_text():
    new_text = "Witaj " + entry.get()
    who = "\nJesteś: " + radio_var.get()
    languages = "\nZnasz następujące języki progrmamowania:\n"
    for i in range(len(checkbox_vars)):
        if checkbox_vars[i].get() == 1:
            languages = languages + " " + checkboxes[i].cget("text")
    experience = "\nmasz "+ str(slider.get()) + " lat doświadczenia."
    home = "\nMieszkasz w województwie:\t" + combobox.get()
    label.config(text=new_text + who + languages + experience + home)

root = tk.Tk()
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}")
root.resizable(width=False, height=False)

root.title("Book Store")
root.geometry("800x600")

root.iconbitmap("./bookshelf.ico")

# label = tk.Label(root, text="Podaj imię i nazwisko:")
# label.pack()
#
# entry = tk.Entry(root)
# entry.pack()
#
# button = tk.Button(root, text="Ok", command=change_text)
# button.pack()

root.iconbitmap("./bookshelf.ico")

screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}")

left_frame = tk.Frame(root,borderwidth=4, relief="ridge",width=int(screen_width / 8),height=int(screen_width / 4))
left_frame.pack(side="left",padx=10, pady=10)
left_frame.pack_propagate(0)
right_frame = tk.Frame(root,width=int(screen_width / 4), height=left_frame["height"],borderwidth=4, relief="ridge")
right_frame.pack(side="right",padx=10, pady=10)
right_frame.pack_propagate(0)

entry = tk.Entry(left_frame)
entry.pack(anchor="w",padx=10, pady=10)
button = tk.Button(left_frame, text="Ok", command=change_text)
button.pack(anchor="center",padx=10, pady=10)

label = tk.Label(right_frame, text="podaj dane")
label.pack(padx=10, pady=10)
radio_var = tk.StringVar(value=" ")



radio_button1 = tk.Radiobutton(left_frame, text="tester", variable=radio_var, value="testerem")
radio_button1.pack(anchor="w",padx=10, pady=10)
radio_button2 = tk.Radiobutton(left_frame, text="programista", variable=radio_var, value="programista")
radio_button2.pack(anchor="w",padx=10, pady=10)


checkbox_vars.append(tk.IntVar())
checkbox = tk.Checkbutton(left_frame, text="java", variable=checkbox_vars[0])
checkbox.pack(anchor="w",padx=10, pady=10)
checkboxes.append(checkbox)
checkbox_vars.append(tk.IntVar())
checkbox2 = tk.Checkbutton(left_frame, text="python", variable=checkbox_vars[1])
checkbox2.pack(anchor="w",padx=10, pady=10)
checkboxes.append(checkbox2)

slider = tk.Scale(left_frame, from_=0, to=25, orient=tk.HORIZONTAL)
slider.pack(anchor="w",padx=10, pady=10)

combobox = ttk.Combobox(left_frame, values=values)
combobox.state(["readonly"])
combobox.pack(anchor="w",padx=10, pady=10)


root.mainloop()

