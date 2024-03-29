from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import os, data, calendar
from datetime import datetime


my_user=data.read_csv()
my_user_data=my_user[0]

data.delete_file()

email_str=my_user_data[1]

total_data=data.select_bmi_data(email_str)



def separate_data_by_year(data):
    year_data1 = {}
    for email, date, height, weight, bmi, category in data:
        year = date[:4]  # Extract year from the date
        if year not in year_data1:
            year_data1[year] = []
        year_data1[year].append((date, height, weight, bmi, category))

    unique_years1 = sorted(year_data1.keys())
    return year_data1, unique_years1

year_data, unique_years = separate_data_by_year(total_data)



def separate_data_by_months(year):
    if year != "All Time":
        month_data1 = {}
        for month in year_data[year]:
            date_value = month[0]
            month_name = get_month_name(date_value)
            month_data1.setdefault(month_name, []).append(month)

        unique_month = sorted(month_data1.keys())
        
        return  unique_month, month_data1
    else:
        return None,None




year_graph_data={}
sorted_year_graph_data={}

def year_data_avg(selected):
    global year_graph_data
    global sorted_year_graph_data
    try:
        year_graph_data.clear()
        sorted_year_graph_data.clear()
        if  selected == "All Time":
            for key, value in year_data.items():
                avg=0
                for i in value:
                    avg=avg+i[3]
                avg=round(avg/len(value),2)
                year_graph_data[key]=avg
            sorted_year_graph_data = {k: year_graph_data[k] for k in sorted(year_graph_data, key=lambda x: int(x))}
            
            
        else:
            for key, value in month_value_graph.items():
                avg=0
                for i in value:
                    avg=avg+i[3]
                avg=round(avg/len(value),2)
                year_graph_data[key]=avg
            sorted_year_graph_data = {month_name: year_graph_data[month_name] for month_name in sorted(year_graph_data, key=lambda x: list(calendar.month_name).index(x))}

            
    except  Exception as e:
        if  selected == "All Time":
            for key, value in year_data.items():
                avg=0
                for i in value:
                    avg=avg+i[3]
                avg=round(avg/len(value),2)
                year_graph_data[key]=avg

            sorted_year_graph_data = {k: year_graph_data[k] for k in sorted(year_graph_data, key=lambda x: int(x))}
 
            
        else:
            for key, value in month_value_graph.items():
                avg=0
                for i in value:
                    avg=avg+i[3]
                avg=round(avg/len(value),2)
                year_graph_data[key]=avg
            sorted_year_graph_data = {month_name: year_graph_data[month_name] for month_name in sorted(year_graph_data, key=lambda x: list(calendar.month_name).index(x))}

        
def month_data_graph(selected):
    global sorted_year_graph_data
    global selected_year
    if  selected != 'All Months':
        year_graph_data.clear()
        sorted_year_graph_data.clear()
        for key, value in month_value_graph.items(): 
            if key==selected :
                for i in value:
                    day=str(get_day(i[0]))
                    year_graph_data[day]=i[3]
                

        sorted_year_graph_data = {k: year_graph_data[k] for k in sorted(year_graph_data, key=lambda x: int(x))}

    else:
        year_data_avg(selected_year)

 
 
 
        
def get_day(date_str):
    try:
        # Parse the date string to a datetime object
        date_object = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Extract the day from the datetime object
        day = date_object.day
        
        return day
    except ValueError:
        return "Invalid date format"


def get_month_name(date_str):
    try:
        # Parse the date string to a datetime object
        date_object = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Extract the month from the datetime object
        month_number = date_object.month
        
        # Get the month name as a string
        month_name = date_object.strftime('%B')
        
        return month_name
    except ValueError:
        return "Invalid date format"
    
    

year_data_combobox=[]
year_data_combobox=unique_years
year_data_combobox.insert(0, "All Time")

def  update_data_display():
    global total_data
    global year_data
    global unique_years
    global year_data_combobox
    total_data.clear()
    total_data=data.select_bmi_data(email_str)
    year_data.clear()
    unique_years.clear()
    year_data, unique_years = separate_data_by_year(total_data)
    year_data_combobox.clear()
    year_data_combobox=unique_years
    year_data_combobox.insert(0, "All Time")


month_name=[]
month_names = []
month_value = {}

def month_data_display(selected_year):
    global month_name
    global month_value
    global month_names
    try:
        global month1_combobox
        global data_label
        
        if month1_combobox:
            month1_combobox.destroy()
        if data_label:
            data_label.destroy()
        
        month1_combobox = None
        data_label = None
        month_name.clear()
        month_names.clear()
        month_value.clear()
        month_names, month_value = separate_data_by_months(selected_year)
        month_name = sorted(month_names)
        month_name.insert(0, "All Months")

    except Exception as e:
        month_name.clear()
        month_names.clear()
        month_value.clear()
        month_names, month_value = separate_data_by_months(selected_year)
        month_name = sorted(month_names)
        month_name.insert(0, "All Months")

    


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
        category="Underweight"
        
    elif bmi>18.5 and  bmi<=24.9:
        label2.config(text="Normal")
        label3.config(text="It indicates that you are healthy!")
        category="Normal"
        
    elif bmi>24.9 and bmi<=29.9:
        label2.config(text="Overweight")
        label3.config(text="It indicates that a person is \n slight overweight!\n A doctor may advice to lose some \n weight for health reasons!")
        category="Overweight"
        
    else:
        label2.config(text="Obesity")
        label3.config(text="Health may be at risk, if they do not \n lose weight!")
        category="Obesity"
    update_data(email_str,h,w,bmi,category)
    update_data_display()
        
        
    
def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
    
def update_data(email,height,weight,bmi,category):
    today_date=str(datetime.today().date())

    data.update_today_data1(email,today_date,height,weight,bmi,category)

#icon
image_icon=PhotoImage(file="BMI_calculator\Resources\icon.png")
root.iconphoto(False,image_icon)

#top
top=PhotoImage(file="BMI_calculator\Resources\BMI Calculator.png")
top_image=Label(root, image=top,  bg='white')
top_image.place(x=425,y=10)

frame=Frame(root, width = 510, height = 550)
frame.place(x=50,y=70)

frame1=Frame(root, width = 650, height = 400, bg="white")
frame1.place(x=560,y=50)

label_frame = tk.LabelFrame(root, text="BMI Data",width=500, height=100)
label_frame.place(x=600, y=490)

data_label=Label(root, bg='white', text="BMI Data of ")
data_label.place(x=650,y=450)

month1_combobox = None 
data_label = None
month_value_graph = None
selected_year = None
month_title=None

def on_Year_change(event=None):
    global month1_combobox
    global data_label
    global month_value_graph
    global g_title
    global g_xaxis
    global selected_year
    global month_title
    
    selected_year = year_combobox.get()
    g_title=str(selected_year)
    x,month_value_graph=separate_data_by_months(selected_year)
    year_data_avg(selected_year)
    
    
    if selected_year != "All Time":
        g_xaxis="Months"
        show_graphic()
        table.delete(*table.get_children())
        table_data_insert(selected_year)
        month_data_display(selected_year)
        
        if month1_combobox is None:
            data_label = tk.Label(root, bg='white', text=", ")
            data_label.place(x=870, y=450)
            
            month1_combobox = ttk.Combobox(root, values=month_name, style='NoBorder.TCombobox', state="readonly")
            month1_combobox.set("Months")
            month1_combobox.place(x=880, y=450)
            month_title=str(selected_year)
            month1_combobox.bind("<<ComboboxSelected>>", on_month1_change)
    else:
        g_xaxis="Years"
        show_graphic()
        table.delete(*table.get_children())
        table_data_insert(selected_year)
        if month1_combobox is not None:
            month1_combobox.destroy()
            data_label.destroy()
            month1_combobox = None
            data_label=None

def on_month1_change(event=None):
    global g_title
    global g_xaxis
    global month_title
    t=month_title
    selected_month = month1_combobox.get()
    m=selected_month
    if selected_month != "All Months":
        g_xaxis="Days"
    else:
        g_xaxis="Months"
    g_title=m + ", "+ t
    month_data_graph(selected_month)
    for key in month_value:

        month_value[key]=sorted(month_value[key])
    table.delete(*table.get_children())

    table_data_insert_month(selected_month)

    show_graphic()
        

def logout():
    root.withdraw()
    os.system("python BMI_calculator\Sign_In.py")
    root.destroy()        
    

year_options = year_data_combobox
year_combobox = ttk.Combobox(root, values=year_options, style='NoBorder.TCombobox', state="readonly")
year_combobox.set("Year")
year_combobox.place(x=720,y=450)
# Bind the combobox change event
year_combobox.bind("<<ComboboxSelected>>", on_Year_change)

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
    if my_user_data[2]=='Male':
        img=(Image.open("BMI_calculator\Resources\man.png"))
    else:
        img=(Image.open("BMI_calculator\Resources\women.png"))
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


g_title=None
g_xaxis=None
fig4, ax4 = plt.subplots()
canvas4 = None

def show_graphic():
    plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])
    global fig4
    global ax4
    global canvas4
    global frame1
    global g_title
    global g_xaxis
    try:
        ax4.clear()
        plt.close(fig4)
        canvas4.get_tk_widget().delete("all")
        for widget in frame1.winfo_children():
            widget.destroy()

    
        ax4.plot(list(sorted_year_graph_data.keys()), list(sorted_year_graph_data.values()), label="BMI", marker="o", markerfacecolor="green")
        ax4.set_title("BMI Data Of "+g_title, fontsize=20)
        ax4.set_xlabel(g_xaxis, fontsize=10)
        ax4.tick_params(axis='both', which='major', labelsize=5)
        ax4.set_ylabel("Body Mass Index",fontsize=10)
        for year, sales in sorted_year_graph_data.items():
            ax4.annotate(str(sales), xy=(year, sales), xytext=(5, 5), textcoords='offset points', fontsize=7)
        ax4.legend()

        canvas4 = FigureCanvasTkAgg(fig4, frame1)
        canvas4.draw()
        canvas4.get_tk_widget().config(width=frame1['width'], height=frame1['height'])
        canvas4.get_tk_widget().pack()

    except  Exception as e:
        
        ax4.plot(list(sorted_year_graph_data.keys()), list(sorted_year_graph_data.values()), label="BMI", marker="o", markerfacecolor="green")
        ax4.set_title("BMI Data Of "+g_title, fontsize=20)
        ax4.set_xlabel(g_xaxis, fontsize=10)
        ax4.tick_params(axis='both', which='major', labelsize=5)
        ax4.set_ylabel("Body Mass Index",fontsize=10)
        for year, sales in sorted_year_graph_data.items():
            ax4.annotate(str(sales), xy=(year, sales), xytext=(5, 5), textcoords='offset points', fontsize=7)
        ax4.legend()

        canvas4 = FigureCanvasTkAgg(fig4, frame1)
        canvas4.draw()
        canvas4.get_tk_widget().config(width=frame1['width'], height=frame1['height'])
        canvas4.get_tk_widget().pack()





table = ttk.Treeview(label_frame, columns = ('date', 'height', 'weight','bmi','category'), show = 'headings', height=5)
table.heading('date', text = 'Date')
table.heading('height', text = 'Height')
table.heading('weight', text = 'Weight')
table.heading('bmi', text = 'BMI')
table.heading('category', text = 'Category')
table.pack(fill = 'x', expand = False)

table.column("date", width=120, anchor=tk.CENTER)
table.column("height", width=100, anchor=tk.CENTER)
table.column("weight", width=100, anchor=tk.CENTER)
table.column("bmi", width=100, anchor=tk.CENTER)
table.column("category", width=120, anchor=tk.CENTER)


def table_data_insert(insert_data_year):
    if  insert_data_year == "All Time":
        for row in sorted(total_data):
            row=list(row)
            date=row[1]
            h=row[2]
            w=row[3]
            b=row[4]
            c=row[5]
            table_data=tuple([date,h,w,b,c])
            table.insert('', 'end', values=table_data)
    else:
        for key, value in year_data.items():
            if key == insert_data_year:
                for i in value:
                    table.insert('', 'end', values=i)            



def table_data_insert_month(insert_data_month):
    if  insert_data_month == "All Months":
        for key,value in month_value.items():
            for i in  value:
                table.insert('', 'end', values=i)
    else:
        for key, value in month_value.items():
            if key == insert_data_month:
                for i in value:
                    table.insert('', 'end', values=i)     




Button(root, width=10, pady=7, text='Log out',bg='#57a1f8',fg='white',border=0, command=logout).place(x=1100,y=20)

label_name=Label(root, font="arial 20 bold", bg="white", fg="#000", justify='center', text=my_user_data[0])
label_name.place(x=20,y=0)

age=str(calculate_age(my_user_data[3]))

label_age=Label(root, font="arial 15 bold", bg="white", fg="#000", justify='center', text="Age:"+age)
label_age.place(x=20,y=30)

root.mainloop()