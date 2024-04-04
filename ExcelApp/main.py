
from tkinter import *
from tkinter import ttk
import openpyxl

root = Tk()


# style = ttk.Style(root)
#
# root.call("source", "forest-light.tcl")
# root.call("source", "forest-dark.tcl")
# style.theme_use("forest-dark")

def toggle_mode():
    # if mode_switch.instate(["selected"]):
        pass

def insert_row():
    name = name_entry.get()
    age = int(age_spinbox.get())
    subscription_status = status_combobox.get()
    employment_status = "Employed" if a.get() else "Unemployed"

    path = "C:\\Users\\DELL\\Documents"
    work_book = openpyxl.load_workbook(path)
    sheet = work_book.active
    row_values = [name, age, subscription_status, employment_status]
    sheet.append(row_values)
    work_book.save(path)

    treeView.insert("", END, values=row_values)

    name_entry.delete(0, END)
    name_entry.insert(0, "Name")
def load_data():
    path = "C:\\Users\\DELL\\Documents"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
    for col_names in list_values[0]:
        treeView.heading(col_names, text=col_names)

    for value in list_values[1:]:
        treeView.insert("", END, values=value)

combo_list = ["Subscribed", "Not subscribed", "Other"]

frame = Frame(master=root)
frame.pack()


widget_frame = LabelFrame(master=frame,text="Information")
widget_frame.grid(row=0, column=0, padx=20, pady=10)

name_entry = Entry(master=widget_frame)
name_entry.insert(0, "Name")

name_entry.bind("<FocusIn>", lambda e : name_entry.delete('0', "end"))
name_entry.grid(row=0, column=0, sticky="ew", pady=(0, 5), padx=5)


age_spinbox = Spinbox(widget_frame, from_=18, to=100)
age_spinbox.insert(0, "Age")
age_spinbox.grid(row=1, column=0, sticky="ew", padx=5, pady=5)


status_combobox = ttk.Combobox(master=widget_frame, values=combo_list)
status_combobox.current(0)
status_combobox.grid(row=2, column=0, sticky="ew", padx=5, pady=5)


a = BooleanVar()
checkbutton = ttk.Checkbutton(widget_frame, text="Employed", variable=a)
checkbutton.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

button = Button(widget_frame,text="Insert", command=insert_row)
button.grid(row=4, column=0, sticky="nsew")


separator = ttk.Separator(widget_frame)
separator.grid(row=5, column = 0, padx = (20, 10), pady=10, sticky="ew")

mode_switch = Checkbutton(widget_frame, text="Mode", command = toggle_mode)

treeFrame = Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)

treeScroll = Scrollbar(master=treeFrame)
treeScroll.pack(side="right", fill="y")

cols = ("Name", "Age", "Subscription", "Employment",)
treeView = ttk.Treeview(treeFrame, show="headings", columns=cols, height=13, yscrollcommand=treeScroll.set)

treeView.column("Name", width=100)
treeView.column("Age", width=50)
treeView.column("Subscription", width=100)
treeView.column("Employment", width=100)

treeView.pack()
treeScroll.config(command=treeView.yview)

load_data()

root.mainloop()