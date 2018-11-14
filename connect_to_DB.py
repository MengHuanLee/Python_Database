import mysql.connector
import io
from PIL import Image

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="CTI_DB"
)

mycursor = mydb.cursor()
image = Image.open("pic/cat.1.jpg")
blob_value = open('pic/cat.1.jpg', 'rb').read()


sql = "INSERT INTO phonebook (LastName, FirstName, PhoneNumber, image) VALUES (%s, %s, %s, %s)"
val = ("Li", "Chang", "408-777-2222", blob_value)
mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("SELECT * FROM phonebook")

myresult = mycursor.fetchall()
for x in myresult:
    print(x)

file_like2 = io.BytesIO(myresult[16][4])
img1=Image.open(file_like2)
img1.show()
mycursor.close()
mydb.close()

