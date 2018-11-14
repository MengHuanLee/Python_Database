import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="CTI_DB"
)

mycursor = mydb.cursor()

sql = "INSERT INTO phonebook (LastName, FirstName, PhoneNumber, image) VALUES (%s, %s, %s, %s)"
val = ("Li", "Chang", "408-777-2222", "")
mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("SELECT * FROM phonebook")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)