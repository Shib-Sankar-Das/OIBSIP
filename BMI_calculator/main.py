from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image
import matplotlib.pyplot as plt

root=Tk()
root.title("BMI Calculator")
root.geometry("1200x650+75+25")
root.resizable(False, False)
root.configure(bg="white")




def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    m=h/100
    bmi=round(float(w/m**2),2)
    label1.config(text=bmi)
    
    if bmi<=18.5:
        label2.config(text="Underweight")
        label3.config(text="You have lower weight then normal body!")
        
    elif bmi>18.5 and  bmi<=24.9:
        label2.config(text="Normal")
        label3.config(text="It indicates that you are healthy!")
        
    elif bmi>24.9 and bmi<=29.9:
        label2.config(text="Overweight")
        label3.config(text="It indicates that a person is \n slight overweight!\n A doctor may advice to lose some \n weight for health reasons!")
        
    else:
        label2.config(text="Obes!")
        label3.config(text="Health may be at risk, if they do not \n lose weight!")
        
    


#icon
image_icon=PhotoImage(file="BMI_calculator\Resources\icon.png")
root.iconphoto(False,image_icon)

#top
top=PhotoImage(file="BMI_calculator\Resources\BMI Calculator.png")
top_image=Label(root, image=top,  bg='white')
top_image.place(x=425,y=10)

frame=Frame(root, width = 510, height = 550)
frame.place(x=50,y=70)

#bottom box
Label(frame,width=66,height=22, bg="lightblue").place(x=20, y=190)

#two boxes
box=PhotoImage(file="BMI_calculator\Resources\Rectangle.png")
Label(frame, image=box).place(x=70, y=10)
Label(frame, image=box).place(x=290, y=10)

#scale
scale=PhotoImage(file="BMI_calculator\Resources\scale_320.png")
Label(frame, image=scale, bg="lightblue").place(x=30, y=200)

###########################Slider1###############################
current_value = tk.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    
    size=int(float(get_current_value()))
    size_H=int(size*1.25)
    size_W=int(size*0.15)
    img=(Image.open("BMI_calculator\Resources\man.png"))
    resized_image=img.resize((50+size_W,10+size_H))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=60, y=510-size_H)
    secondimage.image=photo2

style=ttk.Style()
style.configure("TScale",background="white")
slider=ttk.Scale(frame, from_=0, to=220, orient="horizontal", command=slider_changed, variable=current_value, style="TScale")
slider.place(x=95, y=110)
#################################################################

###########################Slider2###############################
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{:.2f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

style2=ttk.Style()
style2.configure("TScale",background="white")
slider2=ttk.Scale(frame, from_=0, to=200, orient="horizontal", command=slider_changed2, variable=current_value2, style="TScale")
slider2.place(x=315, y=110)
#################################################################

#Entry box
Height=StringVar()
Weight=StringVar()
height=Entry(frame, textvariable=Height, width=6, font='arial 30', bg='white',fg='#000', bd=0, justify='center')
height.place(x=80, y=50)
Height.set(get_current_value())

weight=Entry(frame, textvariable=Weight, width=6, font='arial 30', bg='white',fg='#000', bd=0, justify='center')
weight.place(x=300, y=50)
Weight.set(get_current_value2())

label_H=Label(frame, font="arial 10 bold", bg="white", fg="#000", text="Height (cm)")
label_H.place(x=110,y=20)

label_H=Label(frame, font="arial 10 bold", bg="white", fg="#000", text="Weight (kg)")
label_H.place(x=330,y=20)

secondimage=Label(frame,bg="lightblue")
secondimage.place(x=50, y=280)

Button(frame, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=350, y=210)

label1=Label(frame, font="arial 40 bold", bg="lightblue", fg="#fff", justify='center')
label1.place(x=180,y=200)

label2=Label(frame, font="arial 20 bold", bg="lightblue", fg="#000", justify='center')
label2.place(x=280,y=400)

label3=Label(frame, font="arial 10 bold", bg="lightblue", fg="#000", justify='center')
label3.place(x=200,y=450)






root.mainloop()