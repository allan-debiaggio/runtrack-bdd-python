import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

mydb = mysql.connector.connect(
    user = "root",
    password = PASSWORD,
    host = "127.0.0.1",
    database = "LaPlateforme",
)

if mydb != None :
    print("Connection... SET ! WOUUUUUUUUUUUUUUSH !!!")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM etudiant;")

for x in mycursor :
    print(x)

mydb.close()