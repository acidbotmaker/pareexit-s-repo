# run with debugger

import mysql.connector
from config import DB_CONFIG

db_config = DB_CONFIG

if not all([db_config["host"], db_config["user"]]):
    raise ValueError("Database credentials not found!")

try:
    mydb = mysql.connector.connect(**db_config)
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS employee")

    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS info (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), addr VARCHAR(255))"
    )
    mycursor.execute("SELECT COUNT(*) FROM info")
    if mycursor.fetchone()[0] == 0:
        sql = "INSERT INTO info (name, addr) VALUES (%s, %s)"
        values = [("Virat", "India"), ("Rohit", "India"), ("Rachin", "New Zealand")]
        mycursor.executemany(sql, values)
        mydb.commit()
        print(mycursor.rowcount, "records inserted.")
    else:
        print("Table already contains data. Skipping insertion.")

    mycursor.execute("SELECT * FROM info")
    for row in mycursor.fetchall():
        print(row)

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")
finally:
    if "mydb" in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
