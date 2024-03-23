from tkinter import *
from tkinter import messagebox
import os, data

root=Tk()
root.title("BMI Calculator")
root.geometry('925x500+250+100')
root.configure(bg="#fff")
root.resizable(False, False)

#icon
image_icon=PhotoImage(file="BMI_calculator\Resources\icon.png")
root.iconphoto(False,image_icon)

def signin_success():
    root.withdraw()
    os.system("python BMI_calculator\main.py")
    root.destroy()

global login_data
def signin():
    email=user.get()
    password=code.get()
    login_data=data.select_login(email, password)
    if login_data:
        data.create_csv(login_data) #creating csv
        signin_success()
    else:
        warning1.config(text="Email or password not matched!!!")

def  register():
    
    return login_data

img = PhotoImage(file="BMI_calculator\Resources\logo2.png")
Label(root,  image=img, bg='white').place(x=60, y=10)

frame=Frame(root, width = 350, height = 350, bg = "white")
frame.place(x=480,y=70)

heading=Label(frame, text="Sign in", fg='#57a1f8', bg='white', font=("Microsoft YaHei UI Light", 26, 'bold'))
heading.place(x=100, y=10)

######------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')
    warning1.config(text="")
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, "Email")
        

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light", 11))
user.place(x=30,y=80)
user.insert(0, "Email")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

warning1=Label(frame, fg='red', bg='white', font=("Microsoft YaHei UI Light", 10))
warning1.place(x=35, y=110)

######------------------------------------------------

is_password = False

def on_enter_(e):
    global is_showing
    global is_password
    code.delete(0, 'end')
    warning1.config(text="")
    is_password=True
    is_showing = False
    
def on_leave_(e):
    global is_showing
    global is_password
    name=code.get()
    if name=='':
        code.insert(0, "Password")
        is_showing=True
        show_hide()
    is_password=False
    
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light", 11),show='')
code.place(x=30,y=150)
code.insert(0, "Password")
code.bind('<FocusIn>', on_enter_)
code.bind('<FocusOut>', on_leave_)

def show_hide():
    global is_showing
    global is_password
    if is_password :
        if is_showing :
            code.config(show='')
            show_hide_btn.config(image=hide_p)
        else:
            code.config(show='*')
            show_hide_btn.config(image=show_p)
        is_showing = not is_showing
    
show_p=PhotoImage(file="BMI_calculator\Resources\show_small.png")
hide_p=PhotoImage(file="BMI_calculator\Resources\hide_small.png")
show_hide_btn=Button(frame,image=show_p,bg="white",border=0,command=show_hide)
is_showing = True  
show_hide_btn.place(x=280,y=150)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


##############################################################

Button(frame, width=39, pady=7, text='Sign in',bg='#57a1f8',fg='white',border=0, command=signin).place(x=35,y=204)
lable=Label(frame,text="Don't have an account?",fg='black',bg='white',font=("Microsoft YaHei UI Light", 9))
lable.place(x=75,y=270)

def Sign_Up():
    root.withdraw()
    os.system("python BMI_calculator\Sign_Up.py")
    root.destroy()

sign_up=Button(frame, width=6, text='sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=Sign_Up)
sign_up.place(x=215,y=270)

root.mainloop()