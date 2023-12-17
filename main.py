import mysql.connector
import pandas as pd

i = 1


def database_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="peoples"
    )

def insert(user_id, name, gender, email, dob):
    mydb = database_connect()
    mycursor = mydb.cursor()

    sql = "INSERT INTO users (user_id, name, gender, email, dob) VALUES (%s, %s, %s, %s, %s)"
    val = (user_id, name, gender, email, dob)

    mycursor.execute(sql, val)
    mydb.commit()

    global i
    print(f"[{i}] {name} = record inserted...")
    i += 1

def app():
    df = pd.read_csv('peoples.csv')

    for index, row in df.iloc[0:].iterrows():
        insert(row['User_ID'].strip(), f"{row['First'].strip()} {row['Last'].strip()}", row['Gender'].strip(), row['Email'].strip(), row['DOB'].strip())
        

if __name__ == '__main__':
    app()
