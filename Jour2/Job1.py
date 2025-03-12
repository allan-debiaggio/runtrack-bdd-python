import mysql.connector

cnx = mysql.connector.connect(
    user = "root",
    password = "",
    host = "127.0.0.1",
    database = "LaPlateforme",
)

if cnx != None :
    print("MKAY")

cnx.close()