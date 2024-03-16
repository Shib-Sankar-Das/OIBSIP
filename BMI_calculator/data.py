import mysql.connector as MyConn
mydb=MyConn.connect(host="localhost", user="root", password="S_S_Dragon@721", database="bmi_calculator")
db_cursor=mydb.cursor()

def insert_data_login(username,email, gender, Birth_date,password):
    insert_query = "insert into login_data(Username, Email, Gender, Birth_Date, Password) values(%s,%s,%s,%s,%s)"
    insert_value = (username, email, gender,Birth_date,password)
    db_cursor.execute(insert_query,insert_value)


def insert_bmi_data(email, date, height, weight, bmi):
    insert_query = "insert into user_bmi_data(Email, Date, Height, Weight, BMI) values(%s,%s,%s,%s,%s)"
    insert_value = (email, date, height, weight, bmi)
    db_cursor.execute(insert_query,insert_value)
    
    
def  select_login(username, password):
    try:
        data=[]
        query="SELECT * FROM login_data WHERE Username=? AND Password=?"
        db_cursor.execute(query, (username, password))
        for db_data in db_cursor.fetchall():
            data.append(db_data)
        return data
    except Exception as e:
    # Catch any other exception
        print("An error occurred:", e)
        return  None

def  select_bmi_data(email):
    try:
        data=[]
        query="SELECT * FROM user_bmi_data WHERE Email=?"
        db_cursor.execute(query, (email))
        for db_data in db_cursor.fetchall():
            data.append(db_data)
        return data
    except Exception as e:
    # Catch any other exception
        print("An error occurred:", e)
        return  None

#db_cursor.execute("create database BMI_Calculator")

#print("Data Base Created")

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

