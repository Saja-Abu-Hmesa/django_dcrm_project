import mysql.connector 


database = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = 'Saja123#$',
)



#prepare a cursor object 
cursorObject = database.cursor()

# create the database 
cursorObject.execute("CREATE DATABASE company")


print("All Done")