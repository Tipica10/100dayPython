from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _  in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0,password)
    pyperclip.copy(password)
    #the module pyperclip makes this text already copied onto clipboard so all you have to do it is paste it somewhere
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == '' or password == '':
        messagebox.showwarning(title="Oops", message= "Please don't leave fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message= f"These are the details entered: \nEmail: {email} \nPassword: {password}\nIs it ok to add?")
        if is_ok:
            with open(f"../password-manager-start/EmailsPasswords", "a") as doc:
                doc.write(f"{website} | {email} | {password}\n")
                website_input.delete(0,END)
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(width =200, height=200)
tomato = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= tomato)
canvas.grid(column=1,row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)

website_input = Entry(width=35)
website_input.grid(column=1,row=1, columnspan= 2, sticky="ew")
website_input.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(column=0,row=2)

email_input = Entry(width=35)
email_input.grid(column=1,row=2, columnspan= 2, sticky="ew") #stands for east west
email_input.insert(0, "theephiga04@outlook.com")

password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)

password_input = Entry(width=20)
password_input.grid(column=1, row =3, sticky="ew")

generate_button = Button(text= "Generate Password", width=16, command=generate_password)
generate_button.grid(column=2, row =3)

add_button = Button(text="Add", width = 36, command=add)
add_button.grid(column=1, row =4,columnspan=2)

window.mainloop()