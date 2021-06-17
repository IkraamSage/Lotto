from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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

email = txt_email.get()
veri = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'



address = Label(root, text="Address:", font=("MS sans serif", 15), fg="black", bg="yellow")
address.place(x=50, y=250)

address_entry = Entry(root)
address_entry.place(x=300, y=250)

id_number = Label(root, text="ID number:", font=("MS sans serif", 15), fg="black", bg="yellow")
id_number.place(x=50, y=300)



id_number_entry = Entry(root)
id_number_entry.place(x=300, y=300)


def id_number():
    try:
        id = int(id_number_entry.get())
        if len(id_number_entry.get()) == 13:
            pass
    except ValueError:
        messagebox.showerror("error", "Invalid")


        if re.search(veri, email):
            messagebox.showerror("error", "Enter valid email")

verify_button = Button(root, text="Sign Up", command=id_number)
verify_button.place(x=400, y=350)





root.mainloop()

