from tkinter import  *
from tkinter import ttk
window = Tk()

window.title("Data Entry Form")

frame = Frame(window)

# user information
user_info_frame = LabelFrame(master=frame, text="User Information", )

# Label
first_name_label = Label(master=user_info_frame, text="First Name")

last_name_label = Label(master=user_info_frame, text="Last Name")

title_label = Label(master=user_info_frame, text="Title")

age_label = Label(user_info_frame, text="Age")

# nationality_label
# Entry
first_name_entry = Entry(master=user_info_frame)

last_name_entry = Entry(user_info_frame)

title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Mrs.", "Dr."])

age_spinbox = ttk.Spinbox(user_info_frame, from_=18 , to=90)


user_info_frame.grid(row=0, column=1, padx=20, pady=20)


# user info label
first_name_label.grid(row=0, column=0)

last_name_label.grid(row=0, column=1)

title_label.grid(row=0, column=2)

age_label.grid(row=2, column=0)

# user info label
first_name_entry.grid(row=1, column=0)

last_name_entry.grid(row=1, column=1)

title_combobox.grid(row=1, column=2)

age_spinbox.grid(row=3, column=0)
# user information



frame.pack()

window.mainloop()