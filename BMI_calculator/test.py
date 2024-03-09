def BMI_size():
    h=float(Height.get())
    w=float(Weight.get())
    if  (h>0 and w>0):
        m=h/100
        bmi=round(float(w/m**2),2)
        label1.config(text=bmi)
        
        font_params = ("Arial", 40, "bold")

    # Create a Font object
        label_font = font.Font(family=font_params[0], size=font_params[1], weight=font_params[2])
        text_size_pixels = label_font.measure(str(bmi))
        global lable1_size
        lable1_size=int(text_size_pixels/2)
        print(lable1_size)
        
        label1.place(x=180-lable1_size,y=200)
        
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