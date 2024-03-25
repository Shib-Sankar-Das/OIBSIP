from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")


root=Tk()
root.title("Weather App")
root.geometry("900x500+250+100")
root.resizable(False,False)


def getWeather():
    try:
        city=textfield.get()
        place=city.capitalize()
        
        
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        #print(result)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%H %p")
        clock.config(text=current_time)
        name.config(text=place)
        
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+f"&appid={api_key}"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data["main"]["temp"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]
        
        t.config(font=("arial",70,"bold"),text=(temp,"°C"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°C"))
        
        w.config(text=(wind,"km/h"))
        h.config(text=(f"{humidity}%"))
        d.config(text=(description))
        p.config(text=(f"{pressure}hPa"))
    
    except Exception as e:
        print(e)
        clock.config(text="!!!!!!")
        t.config(font=("arial",40,"bold"),text="Invalid\nEntry\n!!!")
    
    

#search box
Search_image=PhotoImage(file="Weather App\Resource\search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=60,y=40)
textfield.focus()

Search_icon=PhotoImage(file="Weather App\Resource\search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
Logo_iage=PhotoImage(file="Weather App\Resource\A3.png")
logo=Label(image=Logo_iage)
logo.place(x=150,y=100)

#Bottom Box
Frame_image=PhotoImage(file="Weather App\Resource\B_box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",30,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=150)
                       

#label
lable1=Label(root,text="Wind",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
lable1.place(x=115,y=400)

lable2=Label(root,text="Humidity",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
lable2.place(x=245,y=400)

lable3=Label(root,text="Description",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
lable3.place(x=440,y=400)

lable4=Label(root,text="Pressure",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
lable4.place(x=660,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=580,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=580,y=250)

w=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef",width=10)
w.place(x=77,y=430)
h=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef",width=10)
h.place(x=225,y=430)
d=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef", width=15)
d.place(x=400,y=430)
p=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef", width=10)
p.place(x=640,y=430)

root.mainloop()