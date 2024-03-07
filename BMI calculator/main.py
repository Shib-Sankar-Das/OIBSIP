from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

#icon
image_icon=PhotoImage(file="Resources\icon.png")
root.iconphoto(False,image_icon)

#top
