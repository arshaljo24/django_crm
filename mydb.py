import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = '',


)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a databse
cursorObject.execute("CREATE DATABASE dcrm")

print("all Done")