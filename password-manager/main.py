from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# Random password generator and copying the password to clipboard.
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symobols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symobols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# Save password corresponding to each website.
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# UI set up.
window = Tk()
window.title("Password generator")
window.config(padx= 50,pady= 50, bg = "white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
log_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=log_img)
canvas.grid(column= 1, row= 0)

# Website widget
website_label = Label(text= "Website:", fg= "black", bg= "white")
website_label.grid(column=0, row=1)
website_input = Entry(width= 40, fg= "black", bg= "white", highlightbackground="white")
website_input.grid(column=1, row=1, columnspan= 2)
website_input.focus()

# Email username widget
email_label = Label(text= "Email/Username:", fg= "black", bg= "white")
email_label.grid(column=0, row=2)
email_input = Entry(width= 40, fg= "black", bg= "white", highlightbackground="white")
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "sagarch700@gmail.com")

# password widget
password_label = Label(text= "Password:", fg= "black", bg= "white")
password_label.grid(column=0, row=3)
password_input = Entry(width= 22, fg= "black", bg= "white", highlightbackground="white")
password_input.grid(column=1, row=3)

# Generate password button
password_button = Button(text="Generate Password", highlightbackground="white", command= generate_password)
password_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", highlightbackground="white", width= 38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()