import customtkinter as ctk


def add_list():
    task_text = entry.get()


    if task_text:
#         create a frame for the task
        task_frame = ctk.CTkFrame(master=scrollable_frame, width=500)
        task_frame.pack(pady=(5,4))

#         Label to display the text --> task text
        task_label = ctk.CTkLabel(master=task_frame, text=task_text, width=300, font=ctk.CTkFont(family="sans-serif", size=18))
        task_label.pack(side= ctk.LEFT, padx=(0, 10))

        entry.delete(0, ctk.END)


        num_widgets = len(scrollable_frame.winfo_children())
        title_label.configure(text="Daily Tasks (" + str(num_widgets) + ")")
#       delete button
        delete_btn = ctk.CTkButton(master=task_frame, text="Delete", command= lambda: delete_fn(task_frame))
        delete_btn.pack(side=ctk.RIGHT)




def delete_fn(task):
    task.destroy()
    # Update title label after deleting a task
    update_title_label()

def update_title_label():
    num_widgets = len(scrollable_frame.winfo_children())
    if num_widgets < 1:
        title_label.configure(text="Daily Tasks")
    else:
        title_label.configure(text=f"Daily Tasks ({num_widgets})")
window = ctk.CTk()
window.geometry("720x450")
window.title("Todo Daily Tasks")

title_label = ctk.CTkLabel(master=window, text="Daily Tasks",
                           font=ctk.CTkFont(family="sans-serif", size=20, weight="bold"))
title_label.pack(pady=10)

first_entry_frame = ctk.CTkFrame(master=window, width=500)
first_entry_frame.pack(pady=20)
entry = ctk.CTkEntry(master=first_entry_frame, width=350, placeholder_text="Add Activity")
entry.grid(column=0, row=0)

add_btn = ctk.CTkButton(master=first_entry_frame, text="Add", command=add_list)
add_btn.grid(column=1, row=0, padx=(10, 0))


# Scrollable frame
scrollable_frame = ctk.CTkScrollableFrame(master=window, width=500)

# checking for the number of elements in the scrollable frame ?

scrollable_frame.pack()



window.mainloop() 
