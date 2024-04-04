import tkinter.ttk

import customtkinter as ck
from CTkTable import *
from CTkSpinbox import *
from tkinter import *

def load_data():
    name = name_entry.get()
    status = status_combobox.get()
    age = age_entry.get()
    role = roll_combo.get()
    content = [
        [name, status, age, role]
    ]
    if agree_checkBtn.get():
        for cont in content:
            treeView.insert("", tkinter.END, values=cont)



cm_values = ["Single", "Married", "Engaged", "Divorced"]
rm_values = ["Projection", "Sound", "Light", "Videography", "Photography", "Streaming"]

window = ck.CTk()



window.title("Judah Temple Media")
window.geometry("720x450")

frame_main = ck.CTkFrame(master=window,)
frame_main.pack(pady=(20, 0),)


personal_frame = ck.CTkFrame(master=frame_main, width=600)
personal_frame.grid(column=0, row=0, sticky="news", pady=(0, 10))

# Configure column and row weights
# frame_main.columnconfigure(0, weight=1)  # Column 0
# frame_main.rowconfigure(0, weight=0)     # Row 0




name_label = ck.CTkLabel(master=personal_frame, text="Name", font=ck.CTkFont(family="sans-serif", size=15, weight="bold"))
name_label.grid(column=0, row=0, sticky="w")

status_label = ck.CTkLabel(master=personal_frame, text="Status", font=ck.CTkFont(family="sans-serif", size=15, weight="bold"))
status_label.grid(column=1, row=0, sticky="w")

age_label = ck.CTkLabel(master=personal_frame, text="Age",  font=ck.CTkFont(family="sans-serif", size=15, weight="bold"))
age_label.grid(column=2, row=0, sticky="w")

name_entry = ck.CTkEntry(master=personal_frame, font=ck.CTkFont(family="sans-serif", size=17), width=200)
name_entry.grid(column=0, row=1, padx=5,)

status_combobox = ck.CTkComboBox(master=personal_frame, values=cm_values, font=ck.CTkFont(family="sans-serif", size=17), width=150)
status_combobox.current_index = 0
status_combobox.grid(column=1, row=1, padx=5, )

age_entry = CTkSpinbox(personal_frame,
          start_value = 15,
          min_value = 0,
          max_value = 90,
                       font=("sans-serif", 17, "bold"),
                       width=200
         )
age_entry.grid(column=2, row=1, padx=5)

info_frame = ck.CTkFrame(master=frame_main, width=600)
info_frame.grid(column=0, row=1, sticky="news")

role_label = ck.CTkLabel(master=info_frame, text="Role" ,font=ck.CTkFont(family="sans-serif", size=15, weight="bold"))
role_label.grid(row=1, column=0)

roll_combo = ck.CTkComboBox(master=info_frame, values=rm_values)
roll_combo.currentIndex = 0
roll_combo.grid(row=2, column=0)


agree_checkBtn = ck.CTkCheckBox(master=info_frame, text="By Checking means you agree to the terms", font=ck.CTkFont(family="sans-serif", size=15, weight="bold"), )
agree_checkBtn.grid(row=2, column=1)

# Now configure padding for widgets in info_frame
for widget in info_frame.winfo_children():
    widget.grid_configure(padx=10)


add_btn = ck.CTkButton(master=frame_main, text="Add", command=load_data)
add_btn.grid(row=3, column=0, columnspan=1, sticky="ew", pady=(30, 0))


# Tree view
value = [
        ["Name", "Age", "Status", "Patent", "Study"],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
[1,2,3,4,5],
         [1,2,3,4,5],
[1,2,3,4,5],
         [1,2,3,4,5],
[1,2,3,4,5],
         [1,2,3,4,5],
[1,2,3,4,5],
         [1,2,3,4,5],
[1,2,3,4,5],
         [1,2,3,4,5]
]



cols = [
    "Name",
    "Status",
    "Age",
    "Role"
]

treeScroll = tkinter.Scrollbar(master=window)
treeScroll.pack(side="right", fill="y")

treeView = tkinter.ttk.Treeview(master=window, show="headings", columns=cols, )




for col in cols:
    treeView.heading(column=col, text=col)
    treeView.column(col, width=180)

treeView.pack()
treeScroll.config(command=treeView.yview)

window.mainloop()