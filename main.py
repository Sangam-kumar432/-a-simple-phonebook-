 
# importing  library
from tkinter import *

# initialize window

phonebook = Tk()
phonebook.geometry('600x400')
phonebook.config(bg='SlateGray3')
phonebook.title('Sangam - AddressBook')
phonebook.resizable(1, 1)


contact_list = [
    ['Sangam', '735****952'],
    ['Rajeev kumar', '916****241']
]
Name = StringVar()
Number = StringVar()

# create frame
frame = Frame(phonebook)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=15)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


#     function to get select value

def selected():
    return int(select.curselection()[0])


#   function to add new contact
def add_contact():
    contact_list.append([Name.get(), Number.get()])
    select_set()


#        function to edit existing contact
#        first select the contact then click on view button
#        then edit the contact and then click on edit button

def edit():
    contact_list[selected()] = [Name.get(), Number.get()]
    select_set()


#      function to delete selected contact
def delete():
    del contact_list[selected()]
    select_set()


#   to view selected contact
#   first select then click on view button
def view():
    name, phone = contact_list[selected()]
    Name.set(name)
    Number.set(phone)


#     exit the phonebook window
def exit_():
    phonebook.destroy()


# empty name and number field
def reset():
    Name.set('')
    Number.set('')


def select_set():
    contact_list.sort()
    select.delete(0, END)
    for name, phone in contact_list:
        select.insert(END, name)


select_set()

#   define buttons
#   labels and entry widget

Label(phonebook, text='NAME', font='arial 12 bold', bg='SlateGray3').place(x=30, y=20)
Entry(phonebook, textvariable=Name).place(x=100, y=20)
Label(phonebook, text='PHONE NO.', font='arial 12 bold', bg='SlateGray3').place(x=30, y=70)
Entry(phonebook, textvariable=Number).place(x=130, y=70)


Button(phonebook, text=" ADD", font='arial 12 bold', bg='SlateGray4', command=add_contact).place(x=50, y=110)
Button(phonebook, text="EDIT", font='arial 12 bold', bg='SlateGray4', command=edit).place(x=50, y=260)
Button(phonebook, text="DELETE", font='arial 12 bold', bg='SlateGray4', command=delete).place(x=50, y=210)
Button(phonebook, text="VIEW", font='arial 12 bold', bg='SlateGray4', command=view).place(x=50, y=160)
Button(phonebook, text="EXIT", font='arial 12 bold', bg='tomato', command=exit_).place(x=300, y=320)
Button(phonebook, text="RESET", font='arial 12 bold', bg='SlateGray4', command=reset).place(x=50, y=310)

phonebook.mainloop()
print("Phonebook interface destroyed")
