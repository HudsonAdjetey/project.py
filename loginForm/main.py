from tkinter import *
from tkinter import messagebox
from tkinter import GROOVE
# window initialization

window = Tk()
window.geometry("400x350")  # sets the size of the window
window.configure(bg="#333333")
window.title("Login Form")

def login():
    username = "hudson"
    password = "hudson1234"

    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if not entered_username or not entered_password:
        messagebox.showerror('Error', 'Please enter both Username and Password')
        return
    
    if entered_username == username and entered_password == password:
        messagebox.showinfo('Success', 'Login Successful!')
    else:
        messagebox.showerror("Failed", "Incorrect credentials")


# Frame = container to house all the other widgets
frame = Frame(master=window, bg="#333333")

# login label
login_label = Label(master=frame, text="Login", pady=30, font=("Arial", 23), bg="#333333", fg="#fff")

# username label
username_label = Label(master=frame, text="Username", padx=3, pady=15, font=("Arial", 16), fg="#fff", bg="#333333")

# username entry
username_entry = Entry(master=frame, font=("Arial", 16))

# password label
password_label = Label(master=frame, text="Password", padx=3, pady=15, font=("Arial", 16), fg="#fff", bg="#333333")

# password entry
password_entry = Entry(master=frame, show="*", font=("Arial", 16))

# button
login_button = Button(frame, text="Click Me",  bg="lightblue", fg="white", font=("Arial", 14), relief="raised", padx=10, pady=5, command=login)
# placing the widget in the window
login_label.grid(row=0, column=1, columnspan=2, sticky="news")
username_label.grid(row=1, column=0, sticky="w")
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0, sticky="w")
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=1, columnspan=2, pady=20)

username_entry.config(relief=GROOVE, bd=2, highlightthickness=2)
password_entry.config(relief=GROOVE, bd=2, highlightthickness=2)
login_button.config(relief=GROOVE, bd=2, highlightthickness=2)


# calling the window -- block code
frame.pack()
window.mainloop()