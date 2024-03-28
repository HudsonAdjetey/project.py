import tkinter

import xlrd
from tkinter import *
from tkinter import ttk
def load_data():
    file_path = "C:\\Users\\DELL\\Documents\\countries.xls"
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0) # Assuming the data is on the first page

    data = []

    for row_index in range(sheet.nrows):
        row_data = sheet.row_values(row_index)
        data.append(row_data)

    tree = ttk.Treeview(master=window, show="headings", columns=data[0] )
    for col_names in data[0]:
        tree.heading(col_names, text=col_names)

    for value_tuple in data[1:]:
        tree.insert("", tkinter.END, values=value_tuple)

    tree.pack(expand=True, fill="y")
    print(data[2])
    return data

window = Tk()
window.title("Excel Viewer")


load_data()

window.mainloop()