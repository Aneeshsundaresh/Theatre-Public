# Master code for Theater manage ment system


import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",password="tiger123")

def createDatabaseTheatre():
    mydb = conn.connect(host="localhost",user="root",password="tiger123")
    mycursor = mydb.cursor()
    mycursor.execute("Drop Database if exists Theatre")
    mycursor.execute("Create Database Theatre") #Creating the databse

def createTableCustomer(): # Creating customer table
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists Customer")
    mycursor.execute("create table Customer(\
    Username varchar(50) primary key,\
    First_Name varchar(100) NOT NULL,\
    Second_Name varchar(100),\
    Last_Name varchar(100) NOT NULL,\
    DOB Date NOT NULL,\
    Mobile_num varchar(15),\
    Gender varchar(1) NOT NULL,\
    Email_id varchar(100),\
    Password varchar(50),\
    Register_Date datetime\
    );")
    mydb.commit()

def createTableGuestCustomer(): # Creating guest table
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists Guest_Customer")
    mycursor.execute("create table Guest_Customer(\
    Serial_number int(10) Primary key,\
    First_name varchar(100),\
    last_name varchar(100),\
    Mobile_num varchar(15),\
    login_date datetime\
    );")
    mydb.commit()

def creatTableTimings(): #Create table for movie name and time #char(12)--original
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists Timings")
    mycursor.execute("CREATE TABLE Timings (\
    Name char(50),\
    Timing1 char(12),\
    Timing2 char(12),\
    Timing3 char(12),\
    Timing4 char(12),\
    Timing5 char(12),\
    Timing6 char(12),\
    Timing7 char(12)\
    )")

    mycursor.execute("insert into Timings Values('The house',1,2,3,4,5,6,7)")
    mycursor.execute("insert into Timings Values('The car',1,2,3,4,5,6,7)")
    mycursor.execute("insert into Timings Values('The tree',1,2,3,4,5,6,7)")
    mycursor.execute("insert into Timings Values('The fruit',1,2,3,4,5,6,7)")
    mycursor.execute("insert into Timings Values('The love',1,2,3,4,5,6,7)")
    mycursor.execute("insert into Timings Values('The pool',1,2,3,4,5,6,7)")
    mycursor.execute("insert into Timings Values('The bird',1,2,3,4,5,6,7)")
    
    mydb.commit()
    
createDatabaseTheatre()
createTableCustomer()
createTableGuestCustomer()
creatTableTimings()

#For Admin
def addmovie():
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    m=input("Enter the movies name:")
    t1=input("enter timing1 :")
    t2=input("enter timing2 :")
    t3=input("enter timing3 :")
    t4=input("enter timing4 :")
    t5=input("enter timing5 :")
    t6=input("enter timing6 :")
    t7=input("enter timing7 :")
    sql_insert_query =""" INSERT INTO Timings (Name,Timing1,Timing2,Timing3,Timing4,Timing5,Timing6,Timing7) \
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
     
    insert_tuple=(m,t1,t2,t3,t4,t5,t6,t7)
    mycursor.execute(sql_insert_query, insert_tuple)
    print("Movies added")
    mydb.commit()
     
def delmovie():
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    m=input("Enter the movies name:")
    mycursor.execute("DELETE FROM timings WHERE name=%s",(m,))
    mydb.commit()
         
     
#For User


def dispmovie():
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from Timings")
    myrecords=mycursor.fetchall()
    for x in myrecords:
         print (x)
      
def bookmovie():
    m=input("Name of the movie:")
    time=input("Timing:")
    
    y = "yes"
    while y == "yes":
        quantity = int(input("No.of tickets [1 ticket = Dhs 30] [max 6]"))
        if quantity > 6:
            print("Only 6 tickets can be purchased at a time")
        elif quantity <= 0:
            print("Please enter this field with a positive integer")
        else:
            cost(quantity)
            break


def cost(quantity):
    price = quantity * 30.00
    discountCode(price)
    
def discountCode(price):
    code = input("Enter Discount code: ")
    if code == 'Get20%':
        price = price-((20/100)*price)
    elif code == 'Get30%':
        price = price-((30/100)*price)
    elif code == 'Get50%':
        price = price-((50/100)*price)
    elif code == "":
        return
    else:
        print("Entered code does not exist")

    print("The total price is:",price) # recipt


    
    
    
#-----------------------------------------------------------

run = "yes"
while run == "yes":
    def init_menu(): # first thing the users are shown
        print("1. Login ")
        print("2. Register ")
        print("3. Guest Login ")
        print("4. Exit ")

        c=int(input("Enter your choice : "))
        if c == 1:
             login_process()
        elif  c == 2:
             registration_process()
        elif c == 3:
             guest_login_process()
        else:
             return


    #login / sign in

    def login_process():
        mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                            database="Theatre") 
        mycursor = mydb.cursor()
        
        user_id = input("Enter your username: ")
        count = mycursor.execute("select count(*) from customer where Username =  '"+user_id+"'")
        l_count = mycursor.fetchone()

        c='yes'
        while (c=='yes'):
        
            if (user_id =='admin'):
               print("1. Add Movie")
               print("2. Delete Movie")
               print("3. Display Movies")
               print("4. Exit")
               choice=int(input("Enter your Choice"))
               if (choice==1):
                    addmovie()
               elif (choice==2):
                    delmovie()
               elif (choice==3):
                    dispmovie()
               elif (choice==4):
                    print ("Exiting")
                    break

            elif l_count[0] >0:
                
                password = input("Enter your password: ")
                p = mycursor.execute("select password from Customer where Username = '"+user_id+"'")
                l_count = mycursor.fetchone()
                
                if l_count[0]==password:
                    
                    print("1. Book Tickets")
                    print("2. Exit")
                    choice=int(input("Enter your Choice"))
                    if (choice==1):
                        dispmovie()
                        bookmovie()
                    elif (choice==3):
                        print("Thank You")
                        break
                    else:
                        break
                        c=input("Do you want to continue[yes or no]:")

                else:
                    print( "Incorrect username/password. ")
                    print( "Try again. ")
                    login_process()
            else:
                print(" Given username was not registered. ")
                init_menu()



    #Registration
            
    def registration_process():
        mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                            database="Theatre") 
        mycursor = mydb.cursor()
        user_id = input("Enter your username :")
        count = mycursor.execute("select count(*) from Customer where Username = '"+user_id+"'")
        l_count = mycursor.fetchone()
       
        if l_count[0]<= 0:
           
            print( " * Required Field(s)")
            Fname=input("Enter your First Name* : ")
            Sname=input("Enter your Second Name : ")
            Lname=input("Enter your Last Name*  : ")
            DOB=input("Enter your date of Birth (Enter in (YYYY-MM-DD) format ) * : ")
            phonenum=input("Enter your Mobile number : ")
            gen=input("Enter your Gender(M/F)* : ")
            email=input("Enter your email id  : ")

            i = 1
            while i <= 3 : #only 3 attempts. 
                passwd = input("Enter password : ")
                cpasswd = input("Confirm your password. : ")
                if passwd != cpasswd  :
                    print ("Wrong Password . Try again.")
                    i=i+1
                else :
                    break
            if i <= 3 :
                mycursor.execute(" insert into Customer values ('"+user_id+"','"+Fname+"', '"+Sname+"','"+Lname+"','"+DOB+"' \
                ,'" +phonenum+"','"+gen+"','" +email+"','"+passwd+"' ,now())")
                mydb.commit()
                print(" Registration process was successful. ")
                print(" please login to continue. ")
                login_process()
        else:        
            print(" Username is already taken ")
            registration_process()



    # guest_Login

    def  guest_login_process():
        mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                            database="Theatre") 
        mycursor = mydb.cursor()
        Fname=input("Enter your firstname*  : ")
        Lname=input("Enter your lastname*  : ")
        phonenum=input("Enter your mobile number : ")
        mycursor.execute("select max(serial_number) from Guest_Customer ")
        l_max = mycursor.fetchone()
        if l_max[0] is None :
            max_num=1
        else:
            max_num=l_max[0] + 1
        mycursor.execute("insert into Guest_Customer values ("+str(max_num)+ ",'"+Fname+"','"+Lname+"','"+phonenum+"',now())")
        mydb.commit()

        dispmovie()
        bookmovie()  # change according to need                    
         
    init_menu()

    mydb.close()



