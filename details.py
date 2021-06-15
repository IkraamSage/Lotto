from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# GUI size and headers
root = Tk()
root.title("banking details")
root.geometry("550x400")
root.config(bg="yellow")

lotto = PhotoImage(file="lottery2.png")

# Show image using label
image = Label(root, image=lotto)
image.place(x=100, y=0)


lbl_account = Label(root, text="Account number:", font=("MS sans serif", 18))
# lbl_account.place(x=)








root.mainloop()
