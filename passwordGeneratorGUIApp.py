from tkinter import *
import random

window = Tk()
window.iconbitmap('285646_lock_icon.ico')
window.title('Password Generator GUI')
window.config(height=500, width=500, background='black')

photo1 = PhotoImage(file='lock.png')
Label (window, image=photo1, bg='black') .place(relx=0.5, rely=0.15, anchor=CENTER)

lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers =            ['0','1','2','3','4','5','6','7','8','9']
punctual_marks =     ['!','@','#','$','%','^','&','*']

Label (window, text='Choose your preferred options', bg='black', fg='white', font='none 12 bold') .place(relx=0.27, rely=0.33, anchor=CENTER)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = StringVar()
Checkbutton(window, text='Include lower case letters',anchor=W, width=20 ,variable=var1, onvalue=1, offvalue=0) .place(relx=0.21, rely=0.4, anchor=CENTER)
Checkbutton(window, text='Include upper case letters',anchor=W, width=20 ,variable=var2, onvalue=1, offvalue=0) .place(relx=0.21, rely=0.47, anchor=CENTER)
Checkbutton(window, text='Include numbers',anchor=W, width=20 ,variable=var3, onvalue=1, offvalue=0) .place(relx=0.21, rely=0.54, anchor=CENTER)
Checkbutton(window, text='Include punctual marks', anchor=W,width=20 ,variable=var4, onvalue=1, offvalue=0) .place(relx=0.21, rely=0.61, anchor=CENTER)

output = Text(window, width=20, height=15, wrap=WORD, background='white')

def generate_password():
    password = []
    if (var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0):
        if (var1.get() == 1):
            for x in lower_case_letters:
                password.append(x)
        if (var2.get() == 1):
            for x in upper_case_letters:
                password.append(x)
        if (var3.get() == 1):
            for x in numbers:
                password.append(x)
        if (var4.get() == 1):
            for x in punctual_marks:
                password.append(x)
        random.shuffle(password)
        password = ''.join([str(elem) for elem in password])
        print(password)
        output.delete(0.0, END)
        output.insert(END, password)
    else:
        print('Please select password content characters')
        output.delete(0.0, END)
        output.insert(END, 'Please select password content characters')

output.place(relx=0.7, rely=0.62, anchor=CENTER)

Button(window, text='Generate\nPassword', width=8, command=generate_password, font='none 10 bold') .place(relx=0.21, rely=0.75, anchor=CENTER)

# l = Label(window, bg='white', width=20, text='empty')
# l.pack()
 
# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):
#         l.config(text='I love Python ')
#     elif (var1.get() == 0) & (var2.get() == 1):
#         l.config(text='I love C++')
#     elif (var1.get() == 0) & (var2.get() == 0):
#         l.config(text='I do not anything')
#     else:
#         l.config(text='I love both')
 
# var1 = IntVar()
# var2 = IntVar()
# c1 = Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
# c1.pack()
# c2 = Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
# c2.pack()

#CLOSE
def close_window():
    window.destroy()
    exit()

#Label (window, text='Click to exit', bg='black', fg='white', font='none 12 bold') .place(relx=0.1, rely=0.92, anchor=CENTER)
Button(window, text='EXIT', width=6, command=close_window, font='none 10 bold') .place(relx=0.08, rely=0.95, anchor=CENTER)

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

# Label(window, text='Enter the word you would like:', bg='black', fg='white', font='none 12 bold') .grid(row=1, column=0, sticky=W)
# #TEXT_ENTRY/SUBMIT
# textentry = Entry(window, width=20, bg='white')
# textentry.grid(row=2, column=0, sticky=W)
# Button(window, text='SUBMIT', width=6, command=click) .grid(row=3, column=0, sticky=W)

# #LABEL
# Label (window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold') .grid(row=4, column=0, sticky=W)
# #TEXTBOX
# # output = Text(window, width=75, height=6, wrap=WORD, background='white')
# # output.grid(row=5, column=0, columnspan=2, sticky=W)


# from tkinter import *

# window = Tk()
# window.title('Password Generator GUI')
# window.iconbitmap('285646_lock_icon.ico')
# window.config(height=500, width=500, background='black')
# can = Canvas(window, bg = 'black', height=100, width=100)
# can.place(relx=0.5, rely=0.5, anchor=CENTER)
# #photo1 = PhotoImage(file='lock.png')


# #Label (window, image=photo1,height=150, bg='black') .grid(row=0, column=0, sticky=N)

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

# Label(window, text='Enter the word you would like:', bg='black', fg='white', font='none 12 bold') .grid(row=1, column=0, sticky=W)
# #TEXT_ENTRY/SUBMIT
# textentry = Entry(window, width=20, bg='white')
# textentry.grid(row=2, column=0, sticky=W)
# Button(window, text='SUBMIT', width=6, command=click) .grid(row=3, column=0, sticky=W)

# #LABEL
# Label (window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold') .grid(row=4, column=0, sticky=W)
# #TEXTBOX
# # output = Text(window, width=75, height=6, wrap=WORD, background='white')
# # output.grid(row=5, column=0, columnspan=2, sticky=W)

# #CLOSE
# def close_window():
#     window.destroy()
#     exit()

# Label (window, text='click to exit', bg='black', fg='white', font='none 12 bold') .grid(row=6, column=0, sticky=W)
# Button(window, text='EXIT', width=6, command=close_window) .grid(row=8, column=0, sticky=W)

# window.mainloop()
