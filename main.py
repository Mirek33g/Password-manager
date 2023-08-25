from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
  letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  ]
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = randint(8, 10)
  nr_symbols = randint(2, 4)
  nr_numbers = randint(2, 4)

  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)
  password = "".join(password_list)

  input_password.delete(0, END)
  input_password.insert(0, password)
  pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  # users inputs stored in variables
  website = input_website.get()
  email = input_email.get()
  password = input_password.get()

  # checks if any of inputs are empty
  if len(website) == 0 or len(email) == 0:
    messagebox.showinfo(title="Oops",
                        message="Please don't leave any fields empty")
# checks if user agrees with saving details to the file
  else:
    is_ok = messagebox.askokcancel(
      title=website,
      message=
      f"These are the details entered: \nEmal: {email} \nPassword: {password} \nIs it ok to save?"
    )
    if is_ok:
      with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")
        input_website.delete(0, END)
        input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# creates GUI interface (window)
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# adds image on the screen and locate it
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#creates all labes, inputs and buttons to the screen
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

input_website = Entry(width=40)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

input_email = Entry(width=40)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(END, "email@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)

input_password = Entry(width=24)
input_password.grid(column=1, row=3)

generate_button = Button(text="Generate Password",
                         width=12,
                         command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37, command=save)
add_button.grid(column=1, row=4, columnspan=2)
# all labels, inputs and buttuns done

window.mainloop()
