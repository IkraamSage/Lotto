from tkinter import *
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


def convert():
    with open("info.txt", "+a") as written:
        written.write("Account holder name: " + str(txt_name.get()))
        written.write("\n")
        written.write("Account Number: " + str(txt_account.get()))
        written.write("\n")
        written.write("Bank: " + variable.get())
        written.write("\n")
    msg = messagebox.askquestion("You are leaving the claim screen", "Do you want to convert")
    if msg == "yes":
        currency_con()
    else:
        submit()


def submit():
    messagebox.showinfo("Thank you for playing", " An email will be sent soon.")
    read_text_file = 'info.txt'
    read_file = open(read_text_file, "r")
    list_file = read_file.readlines()

    email = str(list_file)
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", email)
    email = emails[-1]
    print(email)

    sender_email_id = 'lotto.sage@gmail.com'
    receiver_email_id = email
    password = "lifechoices2021"
    subject = "Lotto"
    msg = MIMEMultipart()
    msg['From'] = sender_email_id
    msg['To'] = receiver_email_id
    msg['Subject'] = subject
    body = "You've won !1\n"
    f = open("info.txt", "r")
    body = body + f.read()
    f.close()
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(sender_email_id, password)
    print(receiver_email_id)

    # sending the mail
    s.sendmail(sender_email_id, receiver_email_id, text)
    # terminating the session
    s.quit()

check = Button(root, font=("MS sans serif", 18), text="SEND", command=convert)
check.place(x=370, y=260)

def currency_con():
    root.destroy()
    import currency


root.mainloop()
