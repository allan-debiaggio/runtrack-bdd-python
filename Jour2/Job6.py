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

mycursor.execute("SELECT SUM(capacite) FROM salle;")

for _ in mycursor :
    print(f"La capacité de toutes les salles est de : {_[0]}")