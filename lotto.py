from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# GUI size and headers
root = Tk()
root.title("Sign Up")
root.geometry("700x500")
root.config(bg="yellow")

# Add image file
lotto = PhotoImage(file="lottery1.png")

entry1 = Spinbox(root, from_=1, to=49, bg="red", font=("MS sans serif", 18))
entry1.place(x=130, y=180, height=50, width=60)
entry2 = Spinbox(root, from_=1, to=49, bg="green", font=("MS sans serif", 18))
entry2.place(x=210, y=180, height=50, width=60)
entry3 = Spinbox(root, from_=1, to=49, bg="blue", font=("MS sans serif", 18))
entry3.place(x=290, y=180, height=50, width=60)
entry4 = Spinbox(root, from_=1, to=49, bg="orange", font=("MS sans serif", 18))
entry4.place(x=370, y=180, height=50, width=60)
entry5 = Spinbox(root, from_=1, to=49, bg="purple", font=("MS sans serif", 18))
entry5.place(x=460, y=180, height=50, width=60)
entry6 = Spinbox(root, from_=1, to=49, bg="red", font=("MS sans serif", 18))
entry6.place(x=530, y=180, height=50, width=60)

lotto_label = Label(root, bg="red")
lotto_label.place(x=130, y=350, height=50, width=50)
lotto_label = Label(root, bg="green")
lotto_label.place(x=210, y=350, height=50, width=50)
lotto_label = Label(root, bg="blue")
lotto_label.place(x=290, y=350, height=50, width=50)
lotto_label = Label(root, bg="orange")
lotto_label.place(x=370, y=350, height=50, width=50)
lotto_label = Label(root, bg="purple")
lotto_label.place(x=460, y=350, height=50, width=50)
lotto_label = Label(root, bg="red")
lotto_label.place(x=530, y=350, height=50, width=50)
# Show image using label
image = Label(root, image=lotto)
image.place(x=180, y=0)

lucky_num = Label(root, text="Select your lucky numbers", font=("MS sans serif", 20), bg="yellow")
lucky_num.place(x=180, y=120)

play_button = Button(root, text="Play")
play_button.place(x=330, y=270)

exit_btn = Button(root, text="exit")
exit_btn.place(x=580, y=420)

claim_button = Button(root, text="Claim Prize")
claim_button.place(x=100, y=420)



root.mainloop()
