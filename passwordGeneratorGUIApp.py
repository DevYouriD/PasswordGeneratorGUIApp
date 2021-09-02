from tkinter import *
import random

window = Tk()
window.iconbitmap('Resources/285646_lock_icon.ico')
window.title('Password Generator GUI')
window.config(height=500, width=500, background='black')

headerImage = PhotoImage(file='Resources/lock.png')
Label(window, image=headerImage, bg='black').place(relx=0.5, rely=0.16, anchor=CENTER)

lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers =            ['0','1','2','3','4','5','6','7','8','9']
punctual_marks =     ['!','@','#','$','%','^','&','*']

Label(window, text='Choose your preferred options', bg='black', fg='white', font='none 11 bold').place(relx=0.27, rely=0.33, anchor=CENTER)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
Checkbutton(window, text='Include lower case letters',anchor=W, width=20 ,variable=var1, onvalue=1, offvalue=0).place(relx=0.05, rely=0.355)
Checkbutton(window, text='Include upper case letters',anchor=W, width=20 ,variable=var2, onvalue=1, offvalue=0).place(relx=0.05, rely=0.425)
Checkbutton(window, text='Include numbers',anchor=W, width=20 ,variable=var3, onvalue=1, offvalue=0).place(relx=0.05, rely=0.495)
Checkbutton(window, text='Include punctual marks', anchor=W,width=20 ,variable=var4, onvalue=1, offvalue=0).place(relx=0.05, rely=0.565)

Label(window, text='Password length', bg='black', fg='white', font='none 11 bold').place(relx=0.05, rely=0.63)
passwordLength = Scale(window, length=163, from_=5, to=128, orient=HORIZONTAL)

output = Text(window, font='none 12', width=25, height=8, wrap=WORD, background='white')

def generate_password():
    global data
    afterChoiceList = []
    if (var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0):
        if (var1.get() == 1):
            for x in lower_case_letters:
                afterChoiceList.append(x)
        if (var2.get() == 1):
            for x in upper_case_letters:
                afterChoiceList.append(x)
        if (var3.get() == 1):
            for x in numbers:
                afterChoiceList.append(x)
        if (var4.get() == 1):
            for x in punctual_marks:
                afterChoiceList.append(x)

        random.shuffle(afterChoiceList)

        password = []
        for x in range(0,int(passwordLength.get())):
            y = random.randint(0,len(afterChoiceList)-1)
            password.append(afterChoiceList[y])
        random.shuffle(password)
        password = ''.join([str(elem) for elem in password])
        output.delete(0.0, END)
        output.insert(END, '\n' + password)
        data = password
    else:
        output.delete(0.0, END)
        output.insert(END, 'Please select password content characters')

def copy_password():
    try: 
        window.clipboard_clear()
        window.clipboard_append(data)
        print('Copy successfull')
    except NameError:
        print('No password to copy')
        output.delete(0.0, END)
        output.insert(END, 'No password to copy')

def clear_all():
    data = None
    output.delete(0.0, END)

output.place(relx=0.7, rely=0.54, anchor=CENTER)
passwordLength.place(relx=0.05, rely=0.68)

Button(window, text='Generate\nPassword', width=8, command=generate_password, font='none 10 bold').place(relx=0.21, rely=0.845, anchor=CENTER)
Button(window, text='Copy\nPassword', width=8, command=copy_password, font='none 10 bold').place(relx=0.67, rely=0.76, anchor=E)
Button(window, text='Clear\nALL', width=8, command=clear_all, font='none 10 bold').place(relx=0.73, rely=0.76, anchor=W)

#CLOSE
def close_window():
    window.destroy()
    exit()

Button(window, text='EXIT', width=6, command=close_window, font='none 10 bold').place(relx=0.08, rely=0.95, anchor=CENTER)

window.mainloop()
