import mysql.connector as MyConn
import csv, os
mydb=MyConn.connect(host="localhost", user="root", password="S_S_Dragon@721", database="bmi_calculator")
db_cursor=mydb.cursor()
data = []
data1=[]
global userData
userData=[]

def insert_data_login(username,email, gender, Birth_date,password):
    insert_query = "insert into login_data(Username, Email, Gender, Birth_Date, Password) values(%s,%s,%s,%s,%s)"
    insert_value = (username, email, gender, Birth_date, password)
    db_cursor.execute(insert_query,insert_value)
    mydb.commit()
    print("Data Inserted Successfully!")


def insert_bmi_data(email, date, height, weight, bmi):
    insert_query = "insert into user_bmi_data(Email, Date, Height, Weight, BMI) values(%s,%s,%s,%s,%s)"
    insert_value = (email, date, height, weight, bmi)
    db_cursor.execute(insert_query,insert_value)
    mydb.commit()
    

    
    
def select_login(email, password):
    try:
        query = "SELECT * FROM login_data WHERE Email=%s AND Password=%s"
        db_cursor.execute(query, (email, password))
        #data = []
        for db_data in db_cursor.fetchall():
            data.append(db_data) 
        print(data)
        userData=data
        return data
    except Exception as e:
        # Catch any other exception
        print("An error occurred:", e)
        return None


def  select_bmi_data(email):
    try:
        query="SELECT * FROM user_bmi_data WHERE Email=%s"
        db_cursor.execute(query, (email,))
        for db_data in db_cursor.fetchall():
            data1.append(db_data)
        return data1
    except Exception as e:
    # Catch any other exception
        print("An error occurred:", e)
        return  None

#db_cursor.execute("create database BMI_Calculator")


def update_today_data(email,date,height,weight,bmi):
    db_updatedata="update user_bmi_data set Email=%s and Date=%s where Height=%s and Weight=%s and BMI=%s"
    db_value=(email, date, height, weight, bmi)
    db_cursor.execute(db_updatedata,db_value)
    mydb.commit()

#print("Data Base Created")
def create_csv(data):
    file_path='BMI_calculator/Resources/temp.csv'
    # Combine folder path and filename to get full file path
    #file_path = folder_path + '/' + filename
    # Write data to CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)
#create_csv(data)


def read_csv():
    data = []
    file_path='BMI_calculator/Resources/temp.csv'
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def delete_file():
    file_path='BMI_calculator/Resources/temp.csv'
    try:
        os.remove(file_path)
        print(f"File {file_path} successfully deleted.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#delete_file()


sales_year_data = {
    "A": 5000,
    "B": 17500,
    "C": 10000,
    "D": 7500,
    "E": 15000,
    "F": 10000,
    "G": 4000,
    "H": 3000,
    "I": 2000,
    "J": 5000
}

product_data = {
    "A": 10,
    "B": 40,
    "C": 30,
    "D": 20,
    "E": 50
}

