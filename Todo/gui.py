import customtkinter as ctk


def add_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    entry.delete(0, ctk.END)
    label.pack()

root = ctk.CTk()

root.geometry("750x450")
root.title("Todo App")

# TITLE LABEL
title_label = ctk.CTkLabel(master=root, text='Daily Task', font=ctk.CTkFont
    (
    size=30, weight='bold',
    family='sans-serif'
))

title_label.pack(padx=10, pady=(40, 20))

scrollable_frame = ctk.CTkScrollableFrame(root,
                                          width=500,
                                          height=200
                                          )
scrollable_frame.pack()

entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
entry.pack(expand=True, fill="x")

add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo )
add_button.pack(pady=20)
root.mainloop()