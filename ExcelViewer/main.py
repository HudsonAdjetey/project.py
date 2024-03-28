import tkinter

import xlrd
from tkinter import *
from tkinter import ttk
def load_data():
    # workbook

    path = "C:\\Users\\DELL\\Documents\\countries.xls"
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_index(0) # Getting the info from the first page
    print(sheet)
    # Append the data received from the sheet into a list
    # Get the data using the index

    list_container = []

    for row_index in range(sheet.nrows):
        row_values = sheet.row_values(row_index)
        list_container.append(row_values)


    tree_view = ttk.Treeview(master=window, show="headings", columns=list_container[0])
     # loop through the list container to get the header names
    for column_names in list_container[0]:
        tree_view.heading(column_names, text=column_names)

    # Loop through the list container starting from the first index or index one
    for content in list_container[1:]:
        tree_view.insert("", tkinter.END, values=content)

    tree_view.pack(expand=True, fill="y")

window = Tk()
window.title("Excel Viewer")
load_data()
window.mainloop()
