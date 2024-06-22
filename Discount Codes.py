#Discount Codes


import mysql.connector as conn

def createDatabaseTheatre():
    mydb = conn.connect(host="localhost",user="root",password="tiger123")
    mycursor = mydb.cursor()
    mycursor.execute("Drop Database if exists Theatre")
    mycursor.execute("Create Database Theatre")

def createTableCodes():
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre")
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists Discount_Codes")
    mycursor.execute("Create Table if not exists Discount_Codes(Code Char(15))")
    mycursor.execute("insert into Discount_Codes values('Get20%')"   )
    mycursor.execute("insert into Discount_Codes values('Get30%')"   )
    mycursor.execute("insert into Discount_Codes values('Get50%')"   )
    mycursor.execute("insert into Discount_Codes values('TwoForOne')")
    mydb.commit()

createDatabaseTheatre() #Creating the theatre database
createTableCodes()  #Creating the code database


''' +-----------+
    | Code      |
    +-----------+
    | Get20%    |       <---- The Discount_Codes Table
    | Get30%    |
    | Get50%    |
    | TwoForOne |
    +-----------+ '''

#price will be the whatever variable is used to calculate the final result
price = 100 #Example price for now @SatyaGB
 
code = input("Enter Discount code: ")
if code == 'Get20%':
    price = price-((20/100)*price)
elif code == 'Get30%':
    price = price-((30/100)*price)
elif code == 'Get50%':
    price = price-((50/100)*price)
# elif code == 'TwoForOne':
    # Don't know how to do this yet
else:
    print("Entered code does not exist")

print("Final Price", price)

#In Reality this entire Code does not require the database FML

