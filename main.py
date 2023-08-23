from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# creates GUI interface (window)
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# adds image on the screen and locate it 
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file= "logo.png") 
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

input_website = Entry(width=40)
input_website.grid(column=1, row=1, columnspan=2)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

input_email = Entry(width=40)
input_email.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

input_password = Entry(width=24)
input_password.grid(column=1, row=3)

generate_button = Button(text= "Generate Password", width=12)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37)
add_button.grid(column=1, row=4, columnspan=2)









window.mainloop()