from tkinter import *
import string
import random 
import pyperclip
import copy

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_box.get())

    if choice.get() == 1:
        Password_Field.insert(0,random.sample(small_alphabets,password_length))

    if choice.get() == 2:
        Password_Field.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get() == 3:
        Password_Field.insert(0,random.sample(all,password_length))

    # password=random.sample(all,password_length)
    # Password_Field.insert(0,password)

    def copy():
        random_password=Password_Field.get()
        pyperclip.copy(random_password)

root = Tk() 
root.config(bg='gray20')
choice = IntVar()
Font=('arial',13,'bold')
passwordlabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordlabel.grid(pady=10)

weakradioButton=Radiobutton(root,text='weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medum',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

length_label=Label(root,text='Password Length',font=Font,bg='gray20',fg='white')
length_label.grid()

length_box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_box.grid()

Generate_Button=Button(root,text='Generate',font=Font,command=generator)
Generate_Button.grid(pady=5)

Password_Field=Entry(root,width=25,bd=2,font=Font)
Password_Field.grid()

Copy_Button=Button(root,text='Copy',font=Font,command=copy)
Copy_Button.grid(pady=5)

root.mainloop()
