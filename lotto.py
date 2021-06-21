import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


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

def generator():
    first = random.randint(1, 50)
    ref1 = str(first)
    ent1.set(ref1)

    second = random.randint(1, 50)
    ref2 = str(second)
    ent2.set(ref2)

    third = random.randint(1, 50)
    ref3 = str(third)
    ent3.set(ref3)

    fourth = random.randint(1, 50)
    ref4 = str(fourth)
    ent4.set(ref4)

    fifth = random.randint(1, 50)
    ref5 = str(fifth)
    ent5.set(ref5)

    sixth = random.randint(1, 50)
    ref6 = str(sixth)
    ent6.set(ref6)

    generatedList = [first, second, third, fourth, fifth, sixth]
    inputList = [int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get()), int(entry6.get())]
    match = list(set(generatedList).intersection(inputList))
    inter = len(match)
    print(match)
    print(inter)


    if inter <= 1:
        messagebox.showinfo("No matching balls", "You have no winnings")
    elif inter == 2:
        messagebox.showinfo("Well Done!", "You Have won R20")
        message = messagebox.askquestion("You've won", "Do you want to claim prize")
        if message == "yes":
            exit()
    elif inter == 3:
        messagebox.showinfo("Well Done!", "You have won R100.50")
        message = messagebox.askquestion("You've won", "Do you want to claim prize")
        if message == "yes":
            exit()
    elif inter == 4:
        messagebox.showinfo("Well Done!", "You Have Won R2384")
        message = messagebox.askquestion("You've won", "Do you want to claim prize")
        if message == "yes":
            exit()
    elif inter == 5:
        messagebox.showinfo("Well Done!", "You Have Won R8584")
        message = messagebox.askquestion("You've won", "Do you want to claim prize")
        if message == "yes":
            exit()
    else:
        messagebox.showinfo("EXCELLENT!", "YOU'VE WON R10 000 000")
        message = messagebox.askquestion("You've won", "Do you want to claim prize")
        if message == "yes":
            exit()



def exit():
    root.destroy()
    import details
def clear():
    ent1.set("")
    ent2.set("")
    ent3.set("")
    ent4.set("")
    ent5.set("")
    ent6.set("")
    entry1.delete(1, END)
    entry2.delete(1, END)
    entry3.delete(1, END)
    entry4.delete(1, END)
    entry5.delete(1, END)
    entry6.delete(1, END)

ent1 = StringVar()
ent2 = StringVar()
ent3 = StringVar()
ent4 = StringVar()
ent5 = StringVar()
ent6 = StringVar()


lotto_label = Label(root, bg="red", textvariable=ent1)
lotto_label.place(x=130, y=350, height=50, width=50)
lotto_label = Label(root, bg="green", textvariable=ent2)
lotto_label.place(x=210, y=350, height=50, width=50)
lotto_label = Label(root, bg="blue", textvariable=ent3)
lotto_label.place(x=290, y=350, height=50, width=50)
lotto_label = Label(root, bg="orange", textvariable=ent4)
lotto_label.place(x=370, y=350, height=50, width=50)
lotto_label = Label(root, bg="purple", textvariable=ent5)
lotto_label.place(x=460, y=350, height=50, width=50)
lotto_label = Label(root, bg="red", textvariable=ent6)
lotto_label.place(x=530, y=350, height=50, width=50)
# Show image using label
image = Label(root, image=lotto)
image.place(x=180, y=0)

lucky_num = Label(root, text="Select your lucky numbers", font=("MS sans serif", 20), bg="yellow")
lucky_num.place(x=180, y=120)

play_button = Button(root, text="Play", command=generator)
play_button.place(x=330, y=270)

exit_btn = Button(root, text="exit", command=exit)
exit_btn.place(x=580, y=420)

claim_button = Button(root, text="Claim Prize")
claim_button.place(x=100, y=420)

clear_button = Button(root, text="Clear", command=clear)
clear_button.place(x=330, y=420)

root.mainloop()
