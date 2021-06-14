from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# GUI size and headers
root = Tk()
root.title("Sign Up")
root.geometry("700x500")
root.config(bg="yellow")

lucky_num = Label(root, text="Select your lucky numbers", font=("MS sans serif", 20), bg="yellow")
lucky_num.place(x=180, y=100)



root.mainloop()