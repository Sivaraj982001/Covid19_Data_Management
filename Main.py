from sqlite3 import Date
from covid19Data import *
print("#---------------------------------------Covid 19 Data Management System--------------------------------------------------------------------#")

name = input("Enter your user name  : ")
name = name.strip().capitalize()

print("\n#--------------------------------------Search by-------------------------------------------------------------------------------------------#")
print("1. Country")
print("2. Confirmed")
print("3. Deaths")
print("4. Recovered")
print("5. Active")
print("6. Show Table")

search_option = int(input("\nChoose your option : "))

if(search_option == 1):
    Coloumn = "Country"
    Execute(Coloumn,search_option,name)
elif(search_option == 2):
    Coloumn = "Confirmed"
    Execute(Coloumn,search_option,name)
elif(search_option == 3):
    Coloumn = "Deaths"
    Execute(Coloumn,search_option,name)
elif(search_option == 4):
    Coloumn = "Recovered"
    Execute(Coloumn,search_option,name)
elif(search_option == 5):
    Coloumn = "Active"
    Execute(Coloumn,search_option,name)
elif(search_option==6):
    ShowTable()
    print("\n-------------------------------------Thank you for using our Data Management System-------------------------------------------------\n")

    
print("\n----------------------------------------------------------------------------------------------------------------------------------------------")



