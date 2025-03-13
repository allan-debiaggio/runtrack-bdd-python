import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

mydb = mysql.connector.connect(
    user = "root",
    password = PASSWORD,
    host = "127.0.0.1",
    database = "laplateforme",
)

if mydb != None :
    print("CONNEXION ESTABLISHED... WOUUUUUSH !")

mycursor = mydb.cursor()

mycursor.execute("SELECT nom, capacite FROM salle;")

salles = []
    
for x in mycursor :
    salles.append(x)

print(salles)

mydb.close()