from tkinter import *
from modules import get_response
from PIL import Image
from io import BytesIO
import requests

root = Tk()
frame = Frame(root)
frame.pack()

result = StringVar()

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

listbox = Listbox(frame)
listbox.pack()

#whenever i send anything to the ai, the prompt and the response will be shown in the listbox
def call_get_response():
    get_response(entry, result)
    listbox.insert(END, entry.get())
    listbox.insert(END, result.get())

root.mainloop()