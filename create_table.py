import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="peoples"
)

mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE users (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, user_id VARCHAR(50) NOT NULL, name VARCHAR(100) NOT NULL, gender VARCHAR(20) NOT NULL, email VARCHAR(40) NULL, dob VARCHAR(40) NULL)")

print('Table created...')
