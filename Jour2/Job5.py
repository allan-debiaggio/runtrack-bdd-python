import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

mydb = mysql.connector.connect(
    user = "root",
    password = PASSWORD,
    host = "127.0.0.1",
    database = "laplateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT SUM(superficie) FROM etage;")

for x in mycursor :
    
    print(f"La superficie de La Plateforme est de {x[0]} m2")