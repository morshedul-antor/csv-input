import mysql.connector

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
    with open('peoples.txt') as f:
        lines = f.readlines()

        for line in lines: #lines[0:]
            splt = line.split('|')
            insert(splt[0].strip(), f"{splt[1].strip()} {splt[2].strip()}", splt[3].strip(), splt[4].strip(), splt[5].strip())
        

if __name__ == '__main__':
    app()
