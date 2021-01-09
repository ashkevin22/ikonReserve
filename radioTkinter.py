import tkinter as tk

def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    Tk.quit()
    return

root = tk.Tk()

v = tk.IntVar()

tk.Label(root,text="Choose a resort:",justify = tk.LEFT,padx = 20).pack()

radio1 = tk.Radiobutton(root,text="Python",padx = 20,variable=v,value=1).pack(anchor=tk.W)

radio2 = tk.Radiobutton(root,text="Perl",padx = 20,variable=v,value=2).pack(anchor=tk.W)

loginButton = tk.Button(root, text="Submit", )
root.mainloop()