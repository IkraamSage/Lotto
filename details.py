from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# GUI size and headers
root = Tk()
root.title("banking details")
root.geometry("700x360")
root.config(bg="yellow")
variable = StringVar(root)

lotto = PhotoImage(file="lottery2.png")

# Show image using label
image = Label(root, image=lotto)
image.place(x=0, y=0)


lbl_name = Label(root, text="Account holder name:", font=("MS sans serif", 18), bg="yellow")
lbl_name.place(x=220, y=20)

txt_name = Entry(root)
txt_name.place(x=500, y=20)

lbl_account = Label(root, text="Account Number:", font=("MS sans serif", 18), bg="yellow")
lbl_account.place(x=260, y=80)

txt_account = Entry(root)
txt_account.place(x=500, y=80)

bank = Label(root, text="Bank:", font=("MS sans serif", 18), bg="yellow")
bank.place(x=400, y=140)

my_result = StringVar()
variable.set("Select...")
category = OptionMenu(root, variable, 'Standard Bank', 'Capitec', 'Nedbank', "FNB")
category.place(x=500, y=140)


check = Label(root, font=("MS sans serif", 18))
check.place(x=370, y=260)



with open("info.txt", "+a") as written:
    written.write("Account holder name: " + str(txt_name.get()))
    written.write("\n")
    written.write("Account Number: " + str(txt_account.get()))
    written.write("\n")
    written.write("Bank: " + )
    written.write("\n")

def currency_con():
    root.destroy()
    import currency


root.mainloop()
