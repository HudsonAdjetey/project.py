import customtkinter as ck

from CTkSpinbox import *


cm_values = ["Single", "Married", "Engaged", "Divorced"]
rm_values = ["Projection", "Sound", "Light", "Videography", "Photography", "Streaming"]

window = ck.CTk()



window.title("Judah Temple Media")
window.geometry("720x450")

frame_main = ck.CTkFrame(master=window,)
frame_main.pack(pady=(20, 0))

personal_frame = ck.CTkFrame(master=frame_main, width=600)
personal_frame.grid(column=0, row=0, sticky="news", pady=(0, 10))

name_label = ck.CTkLabel(master=personal_frame, text="Name", font=ck.CTkFont(family="sans-serif", size=15, weight="bold"))
name_label.grid(column=0, row=0, sticky="w")

status_label = ck.CTkLabel(master=personal_frame, text="Status", font=ck.CTkFont(family="sans-serif", size=15, weight="bold"))
status_label.grid(column=1, row=0, sticky="w")

age_label = ck.CTkLabel(master=personal_frame, text="Age",  font=ck.CTkFont(family="sans-serif", size=15, weight="bold"))
age_label.grid(column=2, row=0, sticky="w")

name_entry = ck.CTkEntry(master=personal_frame, font=ck.CTkFont(family="sans-serif", size=17), width=200)
name_entry.grid(column=0, row=1, padx=5)

status_combobox = ck.CTkComboBox(master=personal_frame, values=cm_values, font=ck.CTkFont(family="sans-serif", size=17), width=150)
status_combobox.current_index = 0
status_combobox.grid(column=1, row=1, padx=5)

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

agree_checkBtn = ck.CTkCheckBox(master=info_frame, text="By Checking means you agree to the terms", font=ck.CTkFont(family="sans-serif", size=15, weight="bold"))
agree_checkBtn.grid(row=2, column=1)

# Now configure padding for widgets in info_frame
for widget in info_frame.winfo_children():
    widget.grid_configure(padx=10)


add_btn = ck.CTkButton(master=frame_main, text="Add")
add_btn.grid(row=3, column=0, columnspan=1, sticky="ew", pady=(30, 0))


# Tree view
tree_view =

window.mainloop()