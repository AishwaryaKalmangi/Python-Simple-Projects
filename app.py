from time import strftime
from tkinter import Label, Tk
from tkinter import *

# ======= Configuring window =========
window = Tk()
window.title("Digital Clock") #======Text displayed on the window popup=====
window.geometry("500x300") #=======Window pop up size========
window.configure(bg="blue")  # =======Background of the clock=====
window.resizable(False, False)  # =====setting a fixed window size =======
var = StringVar()
clock_label = Label(
    window,bg="black", fg="White", font=("Arial", 60, "bold"), relief="flat", text='center',anchor="center",cursor="dot",
)
clock_label1 = Label(
    window,bg="black", padx="30",textvariable=var,fg="Yellow", font=("Arial", 30, "bold"), relief="flat", text='center',anchor="center",cursor="dot",
)
clock_label1.place(x=700, y=100)
clock_label.place(x=700, y=300)
var.set("This is a Digital Clock")

def update_label():
    """
    This function will update the clock

    every 80 milliseconds
    """
    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)#callback
    #clock_label.pack(anchor="center")


update_label()
window.mainloop()

# ==============The end by github.com/kalebu ==========
