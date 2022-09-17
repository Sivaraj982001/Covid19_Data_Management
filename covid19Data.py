import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@Siva8124",
  database="mydatabase"
)

Cursor = mydb.cursor()

#TableName = "covid19"
#Cursor.execute("DROP TABLE IF EXISTS %s"%(TableName))
#Cursor.execute("""CREATE TABLE IF NOT EXISTS %s (Country VARCHAR(200),Confirmed INT, Deaths INT,Recovered INT,Active INT)"""%(TableName))
#Covid data has been uploaded using workbenc from CSV file to mydatabase
#mydb.commit()

def ShowTable():
    Cursor.execute("SELECT * FROM covid19")
    for i in Cursor:
        print(i)

def Fetch(column, row, Data):
    Cursor.execute(f"SELECT {column} FROM covid19 WHERE {row}={Data}")
    for i in Cursor:
        i = str(i)
        i = i[1:len(i)-2]
        return(i)

def updateData(newData, coloum, data, row):
    Cursor.execute(f"UPDATE covid19 SET {row}={newData} where {coloum}={data}")
    mydb.commit()

def Execute(Coloumn,search_option,name):
    if search_option == 1:
        ColoumnData = input("Enter the Known (referance) Data : ")
        ColoumnData = "'%s'"%(ColoumnData)
    else :
        ColoumnData = int(input("Enter the Known (referance) Data : "))

    Access_Coloumn = input("Enter what coloumn you want to access in that Data Row : ")
    print("-------------------------------------options Menu-------------------------------------------------------------------------")
    print("1. Modify")
    print("2. print only")
    op = int(input("Enter your option : "))
    if(op == 1):
        AP = int(input("Enter your Admin Password : "))
        pin = 1234
        if(AP == pin):
            if(Access_Coloumn == "Country"):
                newData = input("Enter the new Data : ")
                updateData(coloum=Coloumn,row=Access_Coloumn,data=ColoumnData,newData=newData)
            else:
                newData = int(input("Enter the new Data : "))
                updateData(coloum=Coloumn,row=Access_Coloumn,data=ColoumnData,newData=newData)
            print("Your Data has been updated")
            print("Thank you for using our Data management System")
        else:
            print("you may Try again")

    if(op==2):
        print(f"{name},This is your Data {Fetch(column=Coloumn,row=Access_Coloumn,Data=ColoumnData)}")

