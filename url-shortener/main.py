from tkinter import *
import pyshorteners


window = Tk()
window.title("URL shortener")
window.geometry("300x150")

def shortUrl ():
    short =  pyshorteners.Shortener()
    short_url = short.tinyurl.short(longurl_entry.get())
    short_entry.insert(0, short_url)
# widget

longurl_label = Label(master=window, text="Enter Long URL")
longurl_entry = Entry(master=window)
shorturl_label = Label(window, text="Output shortened URL")
short_entry = Entry(master=window)
button_click = Button(master=window, text="Shorten Url", command=shortUrl)

# packing the widgets

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
short_entry.pack()
button_click.pack()

window.mainloop()