import random
from datetime import datetime, timedelta

def calculate_bmi(height, weight):
    return weight / ((height/100) ** 2)

def generate_email():
    return random.choice(["ABC@gmail.com", "simakar@gmail.com"])

def generate_date():
    start_date = datetime(1970, 1, 1)
    end_date = datetime(2024, 1, 1)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')

data = []

for _ in range(100):
    email = generate_email()
    date = generate_date()
    height = round(random.uniform(150, 200), 2)  # Height in cm
    weight = round(random.uniform(50, 100), 2)   # Weight in kg
    bmi = round(calculate_bmi(height, weight), 2)
    data.append((email, date, height, weight, bmi))

print(data)
