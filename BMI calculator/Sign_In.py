from tkinter import *
from tkinter import messagebox
import os

root=Tk()
root.title("BMI Calculator")
root.geometry('925x500+300+100')
root.configure(bg="#fff")
root.resizable(False, False)

def signin_success():
    root.withdraw()
    os.system("python main.py")
    root.destroy()

def signin():
    username=user.get()
    password=code.get()
    
    if username == 'admin' and password == '1234' :
        print("Hi")
        signin_success()

img = PhotoImage(file="Resources\logo2.png")
Label(root,  image=img, bg='white').place(x=60, y=10)

frame=Frame(root, width = 350, height = 350, bg = "white")
frame.place(x=480,y=70)

heading=Label(frame, text="Sign in", fg='#57a1f8', bg='white', font=("Microsoft YaHei UI Light", 26, 'bold'))
heading.place(x=100, y=10)

######------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, "Username")
        

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light", 11))
user.place(x=30,y=80)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

######------------------------------------------------

def on_enter_(e):
    code.delete(0, 'end')
    
def on_leave_(e):
    name=code.get()
    if name=='':
        code.insert(0, "Password")
        
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light", 11))
code.place(x=30,y=150)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter_)
code.bind('<FocusOut>', on_leave_)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##############################################################

Button(frame, width=39, pady=7, text='Sign in',bg='#57a1f8',fg='white',border=0, command=signin).place(x=35,y=204)
lable=Label(frame,text="Don't have an account?",fg='black',bg='white',font=("Microsoft YaHei UI Light", 9))
lable.place(x=75,y=270)

sign_up=Button(frame, width=6, text='sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215,y=270)

root.mainloop()