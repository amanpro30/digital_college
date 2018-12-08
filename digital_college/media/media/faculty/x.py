import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="harshith",
  passwd="12345",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers "



mycursor.execute(sql)


myresult = mycursor.fetchall()


for x in myresult:
  print(x,end="\n")