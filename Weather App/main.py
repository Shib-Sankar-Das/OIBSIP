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


Weather_icon = {
    
    "01d":"Weather App\Resource\icons\Clear sky_01d.png",  # Clear sky day  
    "02d":"Weather App\Resource\icons\Few clouds_02d.png",            # Few clouds day
    "03d":"Weather App\Resource\icons\03d.png",            # Scattered clouds day
    "04d":"Weather App\Resource\icons\Broken clouds_04dn.png",            # Broken clouds day
    "09d":"Weather App\Resource\icons\Shower rain_09dn.png",           # Shower rain day
    "10d":"Weather App\Resource\icons\Rain_10d.png",            # Rain day
    "11d":"Weather App\Resource\icons\Thunderstorm_11dn.png",           # Thunderstorm day
    "13d":"Weather App\Resource\icons\Snow_13dn.png",           # Snow day
    "50d":"Weather App\Resource\icons\Mist_50d.png",       # Mist day
    
    "01n":"Weather App\Resource\icons\Clear sky_01n.png",  # Clear sky day  
    "02n":"Weather App\Resource\icons\Few clouds_02n.png",            # Few clouds day
    "03n":"Weather App\Resource\icons\Scattered clouds_03n.png",            # Scattered clouds day
    "04n":"Weather App\Resource\icons\Broken clouds_04dn.png",            # Broken clouds day
    "09n":"Weather App\Resource\icons\Shower rain_09dn.png",           # Shower rain day
    "10n":"Weather App\Resource\icons\Rain_10n.png",            # Rain day
    "11n":"Weather App\Resource\icons\Thunderstorm_11dn.png",           # Thunderstorm day
    "13n":"Weather App\Resource\icons\Snow_13dn.png",           # Snow day
    "50n":"Weather App\Resource\icons\Mist_50n.png",       # Mist day
    
}


root=Tk()
root.title("Weather App")
root.geometry("900x500+250+100")
root.resizable(False,False)

image_icon=PhotoImage(file="Weather App\Resource\LW.png")
root.iconphoto(False,image_icon)



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
        temp1 = round(json_data["main"]["temp"] - 273.15,2)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]
        icon = json_data["weather"][0]["icon"]
        
        t.config(font=("arial",70,"bold"),text=(temp,"°C"))
        c.config(text=(condition,"|","FEELS","LIKE",temp1,"°C"))
        
        w.config(text=(wind,"km/h"))
        h.config(text=(f"{humidity}%"))
        d.config(text=(description))
        p.config(text=(f"{pressure}hPa"))
        #print(icon)
        Logo_iage.config(file=Weather_icon[icon])
    
    except Exception as e:
        print(e)
        name.config(text="Location Unknown!!!")
        clock.config(text="!!!!!!")
        Logo_iage.config(file=r"Weather App\Resource\icons\Unknown.png")
        t.config(font=("arial",40,"bold"),text="Invalid\nEntry\n!!!")
        c.config(text="")
        
        w.config(text="...")
        h.config(text="...")
        d.config(text="...")
        p.config(text="...")



def getWeather_location():
    try:
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode("")
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        address=location.address.split(", ")
        city=address[0]
        #print(result)
        print(city)
        
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%H %p")
        clock.config(text=current_time)
        name.config(text=city)
        
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+f"&appid={api_key}"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data["main"]["temp"] - 273.15)
        temp1 =(json_data["main"]["temp"] - 273.15,2)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]
        icon = json_data["weather"][0]["icon"]
        
        t.config(font=("arial",70,"bold"),text=(temp,"°C"))
        c.config(text=(condition,"|","FEELS","LIKE",temp1,"°C"))
        
        w.config(text=(wind,"km/h"))
        h.config(text=(f"{humidity}%"))
        d.config(text=(description))
        p.config(text=(f"{pressure}hPa"))
        #print(icon)
        Logo_iage.config(file=Weather_icon[icon])
    
    except Exception as e:
        print(e)
        name.config(text="Location Unknown!!!")
        clock.config(text="!!!!!!")
        Logo_iage.config(file=r"Weather App\Resource\icons\Unknown.png")
        t.config(font=("arial",40,"bold"),text="Invalid\nEntry\n!!!")
        c.config(text="")
        
        w.config(text="...")
        h.config(text="...")
        d.config(text="...")
        p.config(text="...")   
    

#search box
Search_image=PhotoImage(file="Weather App\Resource\search.png")
myimage=Label(image=Search_image)
myimage.place(x=212,y=20)

textfield=tk.Entry(root,width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=252,y=40)
textfield.focus()

Search_icon=PhotoImage(file="Weather App\Resource\search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=592,y=34)


#mylocation
location_image=PhotoImage(file="Weather App\Resource\location2.png")
mylocation=Button(image=location_image, borderwidth=0, command=getWeather_location)
mylocation.place(x=20,y=20)

#logo
Logo_iage=PhotoImage(file="Weather App\Resource\logo2.png")
logo=Label(image=Logo_iage)
logo.place(x=305,y=100)

Logo_Weather = PhotoImage(file="Weather App\Resource\LW.png")
L_Weather = Label(image=Logo_Weather)
L_Weather.place(x=776,y=30)

#Bottom Box
Frame_image=PhotoImage(file="Weather App\Resource\B_box1.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",30,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",45))
clock.place(x=30,y=200)
                       

#label
lable1=Label(root,text="Wind",font=("Helvetica",15,"bold"),fg="white",bg="#34BEF2")
lable1.place(x=115,y=400)

lable2=Label(root,text="Humidity",font=("Helvetica",15,"bold"),fg="white",bg="#34BEF2")
lable2.place(x=245,y=400)

lable3=Label(root,text="Description",font=("Helvetica",15,"bold"),fg="white",bg="#34BEF2")
lable3.place(x=440,y=400)

lable4=Label(root,text="Pressure",font=("Helvetica",15,"bold"),fg="white",bg="#34BEF2")
lable4.place(x=660,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=615,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=615,y=250)

w=Label(text="...",font=("arial",15,"bold"),bg="#34BEF2",width=10)
w.place(x=77,y=430)
h=Label(text="...",font=("arial",15,"bold"),bg="#34BEF2",width=10)
h.place(x=225,y=430)
d=Label(text="...",font=("arial",15,"bold"),bg="#34BEF2", width=15)
d.place(x=400,y=430)
p=Label(text="...",font=("arial",15,"bold"),bg="#34BEF2", width=10)
p.place(x=640,y=430)

root.mainloop()