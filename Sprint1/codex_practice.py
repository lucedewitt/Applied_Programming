name = input("What is your name? ")
print(f"Your name is {name}.")


import tkinter as tk


def display_age():
    age = age_entry.get()
    age_label.config(text=f"Your age is {age}.")


window = tk.Tk()
window.title("Age Input")

tk.Label(window, text="What is your age?").pack(pady=5)

age_entry = tk.Entry(window)
age_entry.pack(pady=5)

tk.Button(window, text="Submit", command=display_age).pack(pady=5)

age_label = tk.Label(window, text="")
age_label.pack(pady=5)

window.mainloop()
