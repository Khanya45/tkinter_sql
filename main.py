import mysql.connector
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='hospital', auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)


root = Tk()
root.geometry('350x300')

def login():
    mycursor.execute('SELECT user, password FROM tblLogin WHERE user="'+edtUsername.get()+'" AND password="'+edtPassword.get()+'"')
    count = 0
    try:
        for i in mycursor:
          count += 1
        if count>0:
            messagebox.showinfo("", "successfully logged")
        else:
            messagebox.showerror("", "the info supplied is incorrect")
    except:
        messagebox.showerror("", "the info supplied is incorrect")
        edtPassword.delete(0, END)
        edtUsername.delete(0, END)


def newuser():
    count = 0
    mycursor.execute('INSERT INTO tblLogin (user, password) VALUES("'+edtUsername.get()+'","' + edtPassword.get()+'")')
    messagebox.showinfo("", "successfully added")
    mydb.commit()


# mycursor.execute('SELECT * FROM tblLogin')
# for i in mycursor:
#     print(i)


lbUsername = Label(root, text="Username")
lbUsername.place(x=40, y=50)
edtUsername = Entry(root)
edtUsername.place(x=150, y=50)

lbPassword = Label(root, text="Password")
lbPassword.place(x=40, y=90)
edtPassword = Entry(root)
edtPassword.place(x=150, y=90)

btnLogin = Button(root, text="Login", command=login)
btnLogin.place(x=70, y=160)

btnLogin = Button(root, text="New User", command=newuser)
btnLogin.place(x=170, y=160)




root.mainloop()
