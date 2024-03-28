from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import openpyxl
import os


def enter_data():
    accepted = accept_var.get()
    if accepted == "Accepted":

        # user Info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # courses info
            registration_status = reg_status_var.get()
            total_courses = num_courses_spinbox.get()
            total_semesters = num_semester_spinbox.get()

            print("First Name: ", firstname, "Last Name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# courses: ", total_courses, "# Semesters: ", total_semesters)
            print("Registration status: ", registration_status)
            print("---------------------------------------------")

            file_path = "E:\\2024 Tutorials\\python\\python-project-newbie\\data-entry\\data.xlsx"

            if not os.path.exists(file_path):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = [
                    "First Name", "Last Name",
                    "Title", "Age",
                    "Nationality", "# Courses",
                    "# Semesters", "Registration Status"
                ]
                sheet.append(heading)
                workbook.save(file_path)

            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active
            sheet.append([
                firstname, lastname, title, age, nationality, total_courses,total_semesters, registration_status
            ])
            workbook.save(file_path)



        else:
            messagebox.showwarning(title="Error", message="First Name and Last Name are required")
    else:
        messagebox.showwarning(title="Error", message="Accept Condition")


window = Tk()

window.title("Data Entry Form")

frame = Frame(master=window)
frame.pack()
user_info_frame = LabelFrame(master=frame, text="User Information")

user_info_frame.grid(row=0, column=0, padx=20, pady=20)

# label containing -- userInfo
first_name_label = Label(master=user_info_frame, text="First Name")
last_name_label = Label(master=user_info_frame, text="Last Name")
title_label = Label(master=user_info_frame, text="Title")
age_label = Label(user_info_frame, text="Age")
nationality_label = Label(user_info_frame, text="Nationality")

# Entry containing -- userInfo
first_name_entry = Entry(master=user_info_frame)
last_name_entry = Entry(master=user_info_frame)
title_combox = ttk.Combobox(master=user_info_frame, values=["", "Mr", "Mrs", "Dr."])
age_spinbox = Spinbox(master=user_info_frame, from_=18, to=110)
nationality_combobox = ttk.Combobox(user_info_frame,
                                    values=["Africa", "Antarctica", "Asia", "Europe", "North America",
                                            "Oceania"])

# grid containing -- userInfo
first_name_label.grid(row=0, column=0)
last_name_label.grid(row=0, column=1)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
title_label.grid(row=0, column=2)
title_combox.grid(row=1, column=2)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Course Frame
course_frame = LabelFrame(frame, text="Course Information")
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

# Label Containing -- courses
registered_label = Label(master=course_frame, text="Registration Status")
num_courses_label = Label(course_frame, text="# Completed Courses")
num_semester_label = Label(course_frame, text="# Semesters")

# Entry
reg_status_var = StringVar(value="Not Registered")
registered_check = Checkbutton(master=course_frame, text="Currently Registered", variable=reg_status_var,
                               onvalue="Registered", offvalue="Not Registered"
                               )

num_courses_spinbox = Spinbox(course_frame, from_=0, to=float("infinity"))
num_semester_spinbox = Spinbox(course_frame, from_=0, to=float("infinity"))
# Grid containing -- Courses
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)
num_courses_label.grid(row=0, column=1)
num_courses_spinbox.grid(row=1, column=1)
num_semester_label.grid(row=0, column=2)
num_semester_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(pady=5, padx=10)

# Accept
# Label
term_frame = LabelFrame(frame, text="Terms and condition")

# Entry
accept_var = StringVar(value="Not Accepted")
terms_check = Checkbutton(term_frame, text="I accept the terms and conditions.", variable=accept_var,
                          offvalue="Not Accepted", onvalue="Accepted")

# grid containing
term_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)
terms_check.grid(row=0, column=0)

# Button
button = Button(frame, text="Enter Data", command=enter_data)
button.grid(row=3, sticky="news", padx=20, pady=10)

window.mainloop()
