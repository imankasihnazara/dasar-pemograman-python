import tkinter as tk
import hashlib

def register():
    username = username_entry.get()
    password = password_entry.get()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # save the username and hashed password to a file or database
    print(f"Username: {username}\nHashed Password: {hashed_password}")

root = tk.Tk()
root.title("Registration Form")

username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=2, column=1)

root.mainloop()


#membuat menu list harga

import tkinter as tk

def calculate_total():
    food_price = food_price_entry.get()
    drink_price = drink_price_entry.get()
    food_discounted_price = float(food_price) * 0.85
    drink_discounted_price = float(drink_price) * 0.85
    total_price = food_discounted_price + drink_discounted_price
    total_price_label.config(text=f"Total Price: {total_price}")

root = tk.Tk()
root.title("Menu Item List")

food_label = tk.Label(root, text="Food Price:")
food_label.grid(row=0, column=0)

food_price_entry = tk.Entry(root)
food_price_entry.grid(row=0, column=1)

drink_label = tk.Label(root, text="Drink Price:")
drink_label.grid(row=1, column=0)

drink_price_entry = tk.Entry(root)
drink_price_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.grid(row=2, column=1)

total_price_label = tk.Label(root, text="Total Price: ")
total_price_label.grid(row=3, column=0, columnspan=2)

root.mainloop()

#menambahkan animasi GUI tambahan
import turtle

turtle.speed(0)

for i in range(100):
    turtle.forward(i * 2)
    turtle.right(90)

turtle.done()
