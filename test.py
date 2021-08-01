from tkinter import *

window = Tk()
window.iconbitmap('285646_lock_icon.ico')
window.title("Password Generator GUI")
window.config(height=500, width=500, background='black')


# can = Canvas(window, bg = 'black', height=100, width=100)
# can.place(relx=0.5, rely=0.5, anchor=CENTER)

photo1 = PhotoImage(file="lock.png")
Label (window, image=photo1, bg="black") .place(relx=0.5, rely=0.20, anchor=CENTER)



#CLOSE
def close_window():
    window.destroy()
    exit()

#Label (window, text='Click to exit', bg='black', fg='white', font='none 12 bold') .place(relx=0.1, rely=0.92, anchor=CENTER)
Button(window, text='EXIT', width=6, command=close_window) .place(relx=0.08, rely=0.95, anchor=CENTER)

window.mainloop()

# def click():
#     entered_text=textentry.get()
#     output.delete(0.0, END)
#     try:
#         definition = my_compdictionary[entered_text]
#     except:
#         definition = 'Sorry there is no word like that please try again'
#     output.insert(END, definition)

# my_compdictionary = {
#     'algorithm' : 'Step by step instructions', 'bug' : 'Piece of code that causes a program to fail'
# }

# Label(window, text="Enter the word you would like:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
# #TEXT_ENTRY/SUBMIT
# textentry = Entry(window, width=20, bg='white')
# textentry.grid(row=2, column=0, sticky=W)
# Button(window, text='SUBMIT', width=6, command=click) .grid(row=3, column=0, sticky=W)

# #LABEL
# Label (window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold') .grid(row=4, column=0, sticky=W)
# #TEXTBOX
# # output = Text(window, width=75, height=6, wrap=WORD, background='white')
# # output.grid(row=5, column=0, columnspan=2, sticky=W)
