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

address = Label(root, text="Address:", font=("MS sans serif", 15), fg="black", bg="yellow")
address.place(x=50, y=250)

address_entry = Entry(root)
address_entry.place(x=300, y=250)

id_number = Label(root, text="ID number:", font=("MS sans serif", 15), fg="black", bg="yellow")
id_number.place(x=50, y=300)

id_number_entry = Entry(root)
id_number_entry.place(x=300, y=300)

verify_button = Button(root, text="Sign Up")
verify_button.place(x=400, y=350)



root.mainloop()

