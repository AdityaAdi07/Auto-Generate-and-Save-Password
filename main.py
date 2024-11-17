from tkinter import *
from tkinter import messagebox  #not a class but a module
import random
import pyperclip
import json

#----------------------------- SEARCH ACC------------------------------------------#
def on_search():
    srch_ele= web1.get()+var_web.get()
    with open('sdata.jason', 'r') as file:
        data1= json.load(file)
        if srch_ele in data1:
            mail_save= data1[f'{srch_ele}']['email'] # to get the email from dictionary
            pass_save= data1[f'{srch_ele}']['password']
            messagebox.askokcancel(title='Result', message=f'Website: {srch_ele}\n Email: {mail_save}\n Password: {pass_save}' )
        elif srch_ele== var_web.get():
            messagebox.showerror(title='Result', message=' Enter the search website!')

        else:
            messagebox.showerror(title='Result', message=f'{srch_ele} website not found')



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pass1.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'qut.txt', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    for char in range(1, 4):  # here char in range coz in the list there are charecters
        password.append(random.choice(letters))  # here its adding random value in list nxt to each(imp)
    for char in range(1, 4):
        password += random.choice(symbols)  # to already existing code in line 11 its adding symbols randomly
    for int in range(1, 4): # by list comprehension, pass_num= [random.choice(numbers) for _ in range (0,4)]
        password += random.choice(numbers)
    final = ""

    for i in range(0, len(password)):
        final += random.choice(password)  # used similar logic and mixed the final password

    pass1.insert(0, final)
    pyperclip.copy(final)  # copies the generated password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def saving():
    web_save= web1.get()+var_web.get()
    mail_save= user1.get()+var_mail.get()
    pass_save= pass1.get()
    save_data= {web_save:{
        'email': mail_save,
        'password': pass_save
        }
    }
    min_web= len(web_save)
    min_mail= len(mail_save)
    min_pass= len(pass_save)
    if min_pass==0 or min_web<=4 or min_mail<=10:
        messagebox.showwarning(title="Error", message='Please dont leave any field empty')

    elif(min_pass<=4):
        messagebox.showwarning(title='Warning', message='Password cannot be less than 5 character')

    else:
        pop_ans= messagebox.askyesno(title=f'{web_save} confirmation', message=f'Please check again the below details:\n Email:{mail_save}\n Password: {pass_save}')
        if pop_ans is True:
            try:
                with open('sdata.jason', 'r') as data_file:  #append so previous one is not deleted
                    data= json.load(data_file) #reading the old data as a dictionary
            except FileNotFoundError:
                with open('sdata.jason', 'w') as data_file:
                    json.dump(save_data,data_file, indent=2)

            else:
                data.update(save_data)
                with open('sdata.jason', 'w') as data_file: #as we have to write
                    json.dump(data, data_file, indent=2)

            finally:
                web1.delete(0,END)  #to delete so after ADD prev entry is deleted
                user1.delete(0, END)
                pass1.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
win=Tk()
win.title('MANAGE PASSWORD')
win.config(padx=50, pady=20)
can1= Canvas(width=200, height=200, highlightthickness=10)
img= PhotoImage(file='logo.png')
can1.create_image(100,100, image=img)
can1.grid(column=1, row=0)

def on_click(): #forget
    select_opt= var_web.get()




web_name=Label(text=' Website :', font=('arial', 10, 'bold'))
web_name.grid(row=1, column=0)

user_name= Label(text='Email/Username :', font=('arial', 10, 'bold'))
user_name.grid(row=2, column=0)

pass_name= Label(text='Password :', font=('arial', 10, 'bold'))
pass_name.grid(row=3, column=0)

web1= Entry(width=21)
web1.focus() #to pre place cursor at that location
web1.grid(row=1, column=1)
#creating drop down list type
option_web= ['.com', '.in', '.gov', '.edu']
var_web= StringVar(win)
var_web.set(option_web[0])

drop_web= OptionMenu(win, var_web, *option_web, command=on_click)
drop_web.grid(row= 1, column= 2)
drop_web.config(width=12)

user1= Entry(width=21)
#user1.insert(END, "@gmail.com")
user1.grid(row=2, column=1)

option_mail= ['@gmail.com', '@yahoo.com', '@microsoft.com']
var_mail= StringVar(win)
var_mail.set(option_mail[0])
drop_mail= OptionMenu(win, var_mail, *option_mail, command=on_click)
drop_mail.grid(row= 2, column= 2)

pass1= Entry(width=21)
pass1.grid(row=3, column=1)

pass2= Button(text='Generate Password', command=generate)
pass2.grid(row=3, column=2)

add1= Button(text="ADD", width=36, command=saving)
add1.grid(row=4, column=1, columnspan=2)

but3= Button(text='Search', font=('arial', 8), command=on_search)
but3.grid(row=1, column=4 )


win.mainloop()