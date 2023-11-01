# import mysql.connector
import sqlite3
import datetime
# db = mysql.connector.connect(
    # port="3305",
    # host="localhost",
    # user="root",
    # passwd="zxclown",
    # auth_plugin='mysql_native_password',
    # database="gosling_database"
# )

db = sqlite3.connect("test.db")
mycursor = db.cursor()

# для mysql
# mycursor.execute("CREATE TABLE gosling_lit (name VARCHAR(50) NOT NULL, result VARCHAR(100) NOT NULL, id int PRIMARY KEY AUTO_INCREMENT NOT NULL)")

# для sqlite
# mycursor.execute("CREATE TABLE gosling_lit (name VARCHAR(50) NOT NULL, result VARCHAR(100) NOT NULL, id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)")

# db.commit()
if __name__ == "__main__":
    pass
