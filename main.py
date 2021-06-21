from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import rsaidnumber, datetime
from datetime import *
import re
import random


# GUI size and headers
root = Tk()
root.title("Sign Up")
root.geometry("550x400")
root.config(bg="yellow")

# Add image file
lotto = PhotoImage(file="lottery1.png")


# Show image using label
image = Label(root, image=lotto)
image.place(x=100, y=0)


lbl_name = Label(root, text="Enter Name:", font=("MS sans serif", 15), fg="black", bg="yellow")
lbl_name.place(x=50, y=150)

txt_name = Entry(root)
txt_name.place(x=300, y=150)

lbl_email = Label(root, text="Email:", font=("MS sans serif", 15), fg="black", bg="yellow")
lbl_email.place(x=50, y=200)

txt_email = Entry(root)
txt_email.place(x=300, y=200)

address = Label(root, text="Address:", font=("MS sans serif", 15), fg="black", bg="yellow")
address.place(x=50, y=250)

address_entry = Entry(root)
address_entry.place(x=300, y=250)

id_number = Label(root, text="ID number:", font=("MS sans serif", 15), fg="black", bg="yellow")
id_number.place(x=50, y=300)

id_number_entry = Entry(root)
id_number_entry.place(x=300, y=300)

def clear():
    txt_name.delete(0, END)
    txt_email.delete(0, END)
    id_number_entry.delete(0, END)
    address_entry.delete(0, END)

def veri():
    text_file = open("Text_file.txt", "a+")
    text_file.write("Name: " + " " + txt_name.get() + " " + "Email: " + " " + txt_email.get() + " " + "Address: " + " " + address_entry.get() + " " + "Unique ID: " + " " + id_number_entry.get())
    text_file.close()
    try:
        id_number = rsaidnumber.parse(id_number_entry.get())
        age = str((datetime.today() - id_number.date_of_birth) //
              timedelta(days=365.25))
        if int(age) >= 18:
            messagebox.showinfo("verified", "Lets Play")
            root.destroy()
            import lotto
        else:
            messagebox.showinfo("not verified", "Must be over 18")
    except ValueError:
        messagebox.showerror("error", "Please enter valid ID number")

        email_ = txt_email.get()
        if re.search(verify, email_):
            messagebox.showinfo("info", "Email is valid")
        else:
            messagebox.showerror("error", "Invalid Email")




verify_button = Button(root, text="Sign Up", command=veri)
verify_button.place(x=400, y=350)

verify = "^(\w|\.|\_|\-)+[@](\w|\_|\-.)+[.]\w{2,2}$"

clear_button = Button(root, text="Clear", command=clear)
clear_button.place(x=220, y=350)



root.mainloop()

