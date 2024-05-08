from tkinter import *
from tkinter import font
from modules import get_response
from PIL import Image
from io import BytesIO
import requests

root = Tk()
frame = Frame(root)
frame.pack()

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=10)

result = StringVar()

listbox = Listbox(frame)
# making the listbox wider
listbox.config(width=43)
listbox.pack()

entry = Entry(frame, width=50)
entry.pack()

def call_get_response():
    get_response(entry, result)
    listbox.insert(END, entry.get())
    listbox.insert(END, result.get())
    

button = Button(frame, text="Talk to AI", command=call_get_response)
button.pack()

label = Label(frame, textvariable=result)
label.pack()



#whenever i send anything to the ai, the prompt and the response will be shown in the listbox
def call_get_response():
    get_response(entry, result)
    listbox.insert(END, entry.get())
    listbox.insert(END, result.get())

root.mainloop()