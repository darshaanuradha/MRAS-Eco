import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE ElderCo")

print("Database Created!")