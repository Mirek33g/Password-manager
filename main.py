from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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


#-------------------FIND PASSWORD -----------------------------------#


def find_password():
  website = input_website.get()
  try:
    with open("data.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No Data File Found")
  else:
    if website in data:
      email = data["website"]["email"]
      password = data["website"]["password"]
      messagebox.showinfo(title=website,
                          message=f"Email: {email}\nPassword: {password}")
    else:
      messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  # users inputs stored in variables
  website = input_website.get()
  email = input_email.get()
  password = input_password.get()
  new_data = {
    website: {
      "email": email,
      "password": password,
    }
  }

  # checks if any of inputs are empty
  if len(website) == 0 or len(email) == 0:
    messagebox.showinfo(title="Oops",
                        message="Please don't leave any fields empty")
# saves details into json file
  else:
    try:
      with open("data.json", "r") as file:
        data = json.load(file)

    except FileNotFoundError:
      with open("data.json", "w") as file:
        json.dump(new_data, file, indent=4)

    else:
      data.update(new_data)
      with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    finally:
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

input_website = Entry(width=24)
input_website.grid(column=1, row=1)
input_website.insert(END, "facebook")
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

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)
# all labels, inputs and buttuns done

window.mainloop()
