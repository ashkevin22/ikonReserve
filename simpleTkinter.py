from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	tkWindow.quit()
	return

#window
tkWindow = Tk()
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="Email").grid(row=0, column=0)
nameVar = StringVar()
usernameEntry = Entry(tkWindow, textvariable=nameVar).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
passVar = StringVar()
passwordEntry = Entry(tkWindow, textvariable=passVar, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, nameVar, passVar)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()