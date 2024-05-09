from tkinter import *
from tkinter import font
from modules import get_response

root = Tk()
frame = Frame(root)
frame.pack()

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=10)

result = StringVar()

# Use a Text widget instead of a Listbox
text = Text(frame, width=50, wrap=WORD)
text.pack()

entry = Entry(frame, width=50)
entry.pack()

def call_get_response():
    get_response(entry, result)
    # Insert the user's message and the AI's response into the Text widget
    text.insert(END, "User: " + entry.get() + '\n')
    text.insert(END, "AI: " + result.get() + '\n')

button = Button(frame, text="Talk to AI", command=call_get_response)
button.pack()

root.mainloop()