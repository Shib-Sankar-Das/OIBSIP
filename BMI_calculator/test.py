import random, data
from datetime import datetime, timedelta

def calculate_bmi(height, weight):
    BMI=round(weight / ((height/100) ** 2),2)
    if BMI<=18.5:
        remarks= "Underweight"
    elif BMI>18.5 and BMI<=24.9:
        remarks="Normal"
    elif BMI>24.9 and BMI<=29.9:
        remarks="Overweight"
    else:
        remarks="Obesity"
        
        
    return BMI, remarks

def generate_email():
    return random.choice(["ABC@gmail.com", "simakar@gmail.com"])

def generate_date():
    start_date = datetime(1970, 1, 1)
    end_date = datetime(2024, 1, 1)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')

data1 = []

for _ in range(10):
    email = generate_email()
    date = generate_date()
    height = round(random.uniform(150, 200), 2)  # Height in cm
    weight = round(random.uniform(50, 100), 2)   # Weight in kg
    bmi, remark = calculate_bmi(height, weight)
    data.insert_bmi_data(email,date,height,weight,bmi,remark)
    data1.append((email, date, height, weight, bmi, remark))

print(data1)
