#My project

from os import close
from tkinter import *
from typing import Sized

#key down function
def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = 'Sorry there is no word like that please try again'
    output.insert(END, definition)

####main:
window = Tk()
window.title("Password Generator GUI")
window.iconbitmap('285646_lock_icon.ico')
photo1 = PhotoImage(file="lock.png")
window.config(background="black")
Label (window, image=photo1,height=150, bg="black") .grid(row=0, column=0, sticky=N)

#create label
Label(window, text="Enter the word you would like:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
#create a text entry box
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky=W)

#add a submit button
Button(window, text='SUBMIT', width=6, command=click) .grid(row=3, column=0, sticky=W)

#create another label
Label (window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold') .grid(row=4, column=0, sticky=W)

#create a text box
output = Text(window, width=75, height=6, wrap=WORD, background='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)
#the dictionary
my_compdictionary = {
    'algorithm' : 'Step by step instructions', 'bug' : 'Piece of code that causes a program to fail'
}
#exit label
Label (window, text='click to exit', bg='black', fg='white', font='none 12 bold') .grid(row=6, column=0, sticky=W)

def close_window():
    window.destroy()
    exit()

Button(window, text='EXIT', width=6, command=close_window) .grid(row=8, column=0, sticky=W)

#####run the main loop
window.mainloop()
