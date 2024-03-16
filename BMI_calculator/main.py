from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_year_data

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

frame1=Frame(root, width = 650, height = 400, bg="red")
frame1.place(x=560,y=50)

label_frame = tk.LabelFrame(root, text="BMI Data",width=500, height=100)
label_frame.place(x=650, y=490)

data_label=Label(root, bg='white', text="BMI Data of ")
data_label.place(x=650,y=450)

month1_combobox = None 
data_label = None

def on_Year_change(event=None):
    global month1_combobox
    global data_label
    
    selected_year = year_combobox.get()
    if selected_year == "2023" or selected_year == "2024":
        if month1_combobox is None:
            data_label = tk.Label(root, bg='white', text=", ")
            data_label.place(x=870, y=450)
            month1_options = ["All Months", 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            month1_combobox = ttk.Combobox(root, values=month1_options, style='NoBorder.TCombobox', state="readonly")
            month1_combobox.set("Months")
            month1_combobox.place(x=880, y=450)
            # Bind the combobox change event
            month1_combobox.bind("<<ComboboxSelected>>", on_month1_change)
    else:
        print("Hello")
        if month1_combobox is not None:
            month1_combobox.destroy()
            data_label.destroy()
            month1_combobox = None
            data_label=None

def on_month1_change(event=None):
    selected_month = month1_combobox.get()
    print("Selected Month:", selected_month)
        
        #on_Year_change()

def on_All_change(event):
    selected_year = year_combobox.get()
    if  selected_year == "All Time":
        print("fre")
        
    

year_options = ["All Time", "2023", "2024"]
year_combobox = ttk.Combobox(root, values=year_options, style='NoBorder.TCombobox', state="readonly")
year_combobox.set("Year")
#year_combobox.pack(pady=10)
year_combobox.place(x=720,y=450)
# Bind the combobox change event
year_combobox.bind("<<ComboboxSelected>>", on_Year_change)
year_combobox.bind("<<ComboboxModified>>", on_All_change)

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


plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Sales by Year", fontsize=20)
ax4.set_xlabel("Year", fontsize=10)
ax4.tick_params(axis='both', which='major', labelsize=5)
ax4.set_ylabel("Sales",fontsize=10)
#plt.show()

canvas4 = FigureCanvasTkAgg(fig4, frame1)
canvas4.draw()
#canvas4.get_tk_widget().pack(side="left", fill="none", expand=False)
#canvas4.get_tk_widget().pack(side="left", fill="both", expand=True, padx=5, pady=5, width=300, height=200)
canvas4.get_tk_widget().config(width=frame1['width'], height=frame1['height'])
canvas4.get_tk_widget().pack()

table = ttk.Treeview(label_frame, columns = ('date', 'height', 'weight','bmi'), show = 'headings', height=5)
table.heading('date', text = 'Date')
table.heading('height', text = 'Hight')
table.heading('weight', text = 'Weight')
table.heading('bmi', text = 'BMI')
table.pack(fill = 'x', expand = False)

table.column("date", width=120, anchor=tk.CENTER)
table.column("height", width=120, anchor=tk.CENTER)
table.column("weight", width=120, anchor=tk.CENTER)
table.column("bmi", width=120, anchor=tk.CENTER)


root.mainloop()