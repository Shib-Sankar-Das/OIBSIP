from tkinter import *
from tkinter import messagebox, ttk
import os
from tkcalendar import DateEntry

root=Tk()
root.title("BMI Calculator")
root.geometry('925x500+250+100')
root.configure(bg="#fff")
root.resizable(False, False)

#icon
image_icon=PhotoImage(file="BMI_calculator\Resources\icon.png")
root.iconphoto(False,image_icon)

def signup_success():
    root.withdraw()
    os.system("python main.py")
    root.destroy()

def signup():
    username=user.get()
    password=code.get()
    
    if username == 'admin' and password == '1234' :
        print("Hi")
        signin_success()

img = PhotoImage(file="BMI_calculator\Resources\h1 (2).png")
Label(root,  image=img, bg='white').place(x=60, y=10)

frame=Frame(root, width = 350, height = 550, bg = "white",)
frame.place(x=480,y=10)

heading=Label(frame, text="Sign up", fg='#57a1f8', bg='white', font=("Microsoft YaHei UI Light", 26, 'bold'))
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

def on_gender_change(event):
    selected_gender = gender_combobox.get()


# Create a style
style = ttk.Style()

# Configure the style for the combobox
style.map('NoBorder.TCombobox',
          fieldbackground=[('readonly', 'white'), ('active', 'white')],
          foreground=[('readonly', 'black'), ('active', 'black')],
          border=[('readonly', 0), ('active', 0)])

# Create a combobox and apply the style
gender_options = ["Male", "Female"]
gender_combobox = ttk.Combobox(frame, values=gender_options, style='NoBorder.TCombobox', state="readonly")
gender_combobox.set("Gender")
gender_combobox.pack(pady=10)

gender_combobox.place(x=30,y=130)
# Bind the combobox change event
gender_combobox.bind("<<ComboboxSelected>>", on_gender_change)

######------------------------------------------------

cal=DateEntry(frame,selectmode='day',date_pattern="dd/mm/y",state="readonly")
cal._set_text("Birth Date")
cal.place(x=200,y=130)

######------------------------------------------------


def on_enter_email(e):
    email.delete(0, 'end')
    
def on_leave_email(e):
    name=email.get()
    if name=='':
        email.insert(0, "Email")

email = Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light", 11))
email.place(x=30,y=190)
email.insert(0, "Email")
email.bind('<FocusIn>', on_enter_email)
email.bind('<FocusOut>', on_leave_email)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=217)

######------------------------------------------------

is_password = False

def on_enter_(e):
    global is_showing
    global is_password
    code.delete(0, 'end')
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
code.place(x=30,y=260)
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
show_hide_btn.place(x=280,y=260)



Frame(frame,width=295,height=2,bg='black').place(x=25,y=287)

######------------------------------------------------

is_password1 = False

def on_enter_1(e):
    global is_showing1
    global is_password1
    code1.delete(0, 'end')
    is_password1=True
    is_showing1 = False
    
def on_leave_1(e):
    global is_showing1
    global is_password1
    name=code1.get()
    if name=='':
        code1.insert(0, "Confirm Password")
        is_showing1=True
        show_hide1()
    is_password1=False
    
code1 = Entry(frame,width=25,fg='black',border=0,bg="white",font=("Microsoft YaHei UI Light", 11),show='')
code1.place(x=30,y=330)
code1.insert(0, "Confirm Password")
code1.bind('<FocusIn>', on_enter_1)
code1.bind('<FocusOut>', on_leave_1)

def show_hide1():
    global is_showing1
    global is_password1
    if is_password1 :
        if is_showing1 :
            code1.config(show='')
            show_hide_btn1.config(image=hide_p1)
        else:
            code1.config(show='*')
            show_hide_btn1.config(image=show_p1)
        is_showing1 = not is_showing1
    
show_p1=PhotoImage(file="BMI_calculator\Resources\show_small.png")
hide_p1=PhotoImage(file="BMI_calculator\Resources\hide_small.png")
show_hide_btn1=Button(frame,image=show_p1,bg="white",border=0,command=show_hide1)
is_showing1 = True  
show_hide_btn1.place(x=280,y=330)



Frame(frame,width=295,height=2,bg='black').place(x=25,y=357)

##############################################################

Button(frame, width=39, pady=7, text='Sign up',bg='#57a1f8',fg='white',border=0, command=signup).place(x=35,y=380)
lable=Label(frame,text="Already have an account?",fg='black',bg='white',font=("Microsoft YaHei UI Light", 9))
lable.place(x=75,y=430)

def sign_in():
    root.withdraw()
    os.system("python BMI_calculator\Sign_In.py")
    root.destroy()

sign_up=Button(frame, width=6, text='sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign_in)
sign_up.place(x=215,y=430)

root.mainloop()