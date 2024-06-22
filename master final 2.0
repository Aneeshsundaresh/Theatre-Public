# Master code for Theater management system

import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002")

#---------Creating part---------------
#----Makes the tables and database----

def createDatabaseTheatre(): #Creating the main database
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002")
    mycursor = mydb.cursor()
    mycursor.execute("Drop Database if exists Theatre") #Drops exsisting database
    mycursor.execute("Create Database Theatre") #Creating the databse

def createTableCustomer(): # Creating customer table
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists Customer") #Drops any exsisting table
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
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists Guest_Customer") #Drop exsisting guest
    mycursor.execute("create table Guest_Customer(\
    Serial_number int(10) Primary key,\
    First_name varchar(100),\
    last_name varchar(100),\
    Mobile_num varchar(15),\
    login_date datetime\
    );")
    mydb.commit()

def creatTableTimings(): #Create table for movie name and time #char(12)--original
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists Timings") #Drop table if exsist
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

    #Has the following movies in the database already
    mycursor.execute("insert into Timings Values('The Haunting ','01:00','04:00','10:00','14:00','16:00','18:00','22:00')")
    mycursor.execute("insert into Timings Values('The Car','02:00','04:00','10:40','14:50','16:00','18:25','22:00')")
    mycursor.execute("insert into Timings Values('Treehouse Stories','01:00','04:50','10:40','14:00','16:55','18:00','22:00')")
    mycursor.execute("insert into Timings Values('Penguin Hero 6','02:00','04:00','12:00','14:00','16:00','18:00','22:00')")
    mycursor.execute("insert into Timings Values('My Little Pony','01:50','07:00','13:00','14:00','16:00','18:00','22:00')")
    mycursor.execute("insert into Timings Values('Panda Man 2','01:00','09:00','11:00','14:00','16:00','18:00','22:00')")
    mycursor.execute("insert into Timings Values('Kung Fu Fighter','01:00','04:00','10:40','14:00','16:00','18:25','22:00')")
    mydb.commit()

createDatabaseTheatre()
createTableCustomer()
createTableGuestCustomer()
creatTableTimings()


#--------Main code Parts------
#---------For User------------

def init_menu(): # first thing the users are shown
    global run , mainrun
    print("1. Login ")
    print("2. Register ")
    print("3. Guest Login ")
    print("4. Exit ")

    c=input("Enter your choice : ")
    if c == "1":
        login_process()
    elif  c == "2":
        registration_process()
    elif c == "3":
        guest_login_process()
    elif c == "4":
        run="No"
        mainrun ="No"
        print(" ")
        print("----Exiting The program. Thank You----")
        print(" ") 
    else:
        print("Option incorrect/unavailable")
        print("")
         

def login_process():  
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    global user_id
    user_id = input("Enter your username : ")
    count = mycursor.execute("select count(*) from customer where Username =  '"+user_id+"'")
    l_count = mycursor.fetchone()

    c='yes'
    while (c=='yes'):
        
        # For admin
        if (user_id =='admin'):
           print(" ")
           print("1. Add Movie")
           print("2. Delete Movie")
           print("3. Display Movies")
           print("4. Exit")
           choice=input("Enter your choice : ")
           if choice=="1":
                addmovie()
           elif choice=="2":
                delmovie()
           elif choice=="3":
                dispmovie()
           elif choice=="4":
                print("Exiting")
                print(" ")
                break
           else:
                print("Option incorrect/unavailable")
                print("")
            

        elif l_count[0]>0:
            
            password = input("Enter your password: ")
            p = mycursor.execute("select password from Customer where Username = '"+user_id+"'")
            l_count = mycursor.fetchone()
            
            if l_count[0]==password:
                
                print("1. Book Tickets")
                print("2. Exit")
                choice=int(input("Enter your choice : "))
                if (choice==1):
                    dispmovie()
                    bookmovie()
                    break
                elif (choice==2):
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
            print("Given username was not registered. ")
            print(" ")
            init_menu()
                
def registration_process():
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    user_id = input("Enter your username : ")
    count = mycursor.execute("select count(*) from Customer where Username = '"+user_id+"'")
    l_count = mycursor.fetchone()
   
    if l_count[0] <= 0:
        
        global Fname
        print( " * Required Field(s)")
        Fname=input("Enter your First Name* : ")
        Sname=input("Enter your Middle Name : ")
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
            mycursor.execute(" insert into Customer values ('"+user_id+"','"+Fname+"',\
                                '"+Sname+"','"+Lname+"','"+DOB+"' ,'" +phonenum+"',\
                                '"+gen+"','" +email+"','"+passwd+"' ,now())")
            
            mydb.commit()
            print(" Registration process was successful. ")
            print(" please login to continue. ")
            login_process()
    else:        
        print(" Username is already taken ")
        registration_process()

def guest_login_process():
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
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
    mycursor.execute("insert into Guest_Customer values ("+str(max_num)+ ",'"+Fname+"','"+Lname+"',\
                        '"+phonenum+"',now())")
    mydb.commit()

    dispmovie()
    bookmovie()         
            
def dispmovie():
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from Timings")
    myrecords=mycursor.fetchall()
    print ('Name of Movie'  + int((50 - len('Name of Movie') ) / 8) * '\t' , 'Timing1' + int((15 - len('Timing1') ) / 8) * '\t',end = '')
    print('Timing2' + int((15 - len('Timing2') ) / 8) * '\t', 'Timing3' + int((15 - len('Timing3') ) / 8) * '\t', 'Timing4' + int((15 - len('Timing4') ) / 8) * '\t', end = '')
    print('Timing5' + int((15 - len('Timing5') ) / 8) * '\t','Timing6' + int((15 - len('Timing6') ) / 8) * '\t','Timing7' + int((15 - len('Timing7') ) / 8) * '\t')
    print('*****************************************************************************************************************************************************')
    for x in myrecords:
       print (x[0] + int((50 - len(x[0]) ) / 8) * '\t' , x[1] + int((15 - len(x[1]) ) / 8) * '\t' , end = ' ')
       print (x[2] + int((15 - len(x[2]) ) / 8) * '\t' , end = ' ')
       print (x[3] + int((15 - len(x[3]) ) / 8) * '\t' , end = ' ')
       print (x[4] + int((15 - len(x[4]) ) / 8) * '\t' , end = ' ')
       print (x[5] + int((15 - len(x[5]) ) / 8) * '\t' , end = ' ')
       print (x[6] + int((15 - len(x[6]) ) / 8) * '\t' , end = ' ')
       print (x[7] + int((15 - len(x[7]) ) / 8) * '\t')
      
def bookmovie():
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    global Movie_Name
    Movie_Name=input("Name of the movie:")
    count = mycursor.execute("select count(*) from timings where Name = '"+Movie_Name+"'")
    l_count = mycursor.fetchone()
    
    if l_count[0] > 0:
            global Time
            Time=input("Timing:")
            count = mycursor.execute("select count(*) from timings where Timing1 = '"+Time+"' or Timing2 = '"+Time+"' or Timing3 = '"+Time+"' or Timing4 = '"+Time+"' or Timing5 = '"+Time+"' or Timing6 = '"+Time+"' or Timing7 = '"+Time+"' ")
            l_count = mycursor.fetchone()
    
            if l_count[0] > 0:
                pass
            else:
                print("That timing is not available ")
                print("Choose movie with that timing ")
                bookmovie()
    else:
        print("That movie is not available")
        print("Enter movie again")
        bookmovie()

    y = "yes"
    while y == "yes":
        global Ticket_Quantity 
        Ticket_Quantity = input("No.of tickets [1 ticket = Dhs 30] [max 6]")
        if Ticket_Quantity == '':
            print("Please enter a value")
        elif int(Ticket_Quantity) > 6:
            print("Only 6 tickets can be purchased at a time")
        elif int(Ticket_Quantity) <= 0:
            print("Please enter this field with a positive integer")
        else:
            y="No"
            cost(int(Ticket_Quantity))
            break

#-------For Admin------
#Has the ability to add or remove movies
def addmovie():
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    m=input("Enter the movies name:")
    t1=input("enter timing1 : ")
    t2=input("enter timing2 : ")
    t3=input("enter timing3 : ")
    t4=input("enter timing4 : ")
    t5=input("enter timing5 : ")
    t6=input("enter timing6 : ")
    t7=input("enter timing7 : ")
    sql_insert_query =""" INSERT INTO Timings (Name,Timing1,Timing2,Timing3,Timing4,Timing5,Timing6,Timing7) \
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
     
    insert_tuple=(m,t1,t2,t3,t4,t5,t6,t7)
    mycursor.execute(sql_insert_query, insert_tuple)
    print("Movie added")
    mydb.commit()

#Removing movies
def delmovie():
    mydb = conn.connect(host="localhost",user="root",password="Aneeshs2002",\
                        database="Theatre") 
    mycursor = mydb.cursor()
    m=input("Enter the movies name:")
    mycursor.execute("DELETE FROM timings WHERE name=%s",(m,))
    mydb.commit()

#---------End of Program Parts--------------

def cost(Total_quantity):
    global Total_Cost
    Total_Cost = Total_quantity * 30.00
    discountCode(Total_Cost)
    
def discountCode(Total_Cost):
    global TotalCostDisc
    global CODE
    y = "yes"
    while y == "yes":
        global CODE
        code = input("Enter Discount code: ")
        if code == 'Get20%':
            TotalCostDisc = Total_Cost-((20/100)*Total_Cost)
            CODE = "YES"
            break
        elif code == 'Get30%':
            TotalCostDisc = Total_Cost-((30/100)*Total_Cost)
            CODE = "YES"
            break
        elif code == 'Get50%':
            TotalCostDisc = Total_Cost-((50/100)*Total_Cost)
            CODE = "YES"
            break
        elif code == "":
            CODE = "NO"
            TotalCostDisc = Total_Cost
            break
        else:
            CODE = "NO"
            TotalCostDisc = Total_Cost
            print("Entered code does not exist")
            
    print(" ")
    receipt()

    
#----Recipt-----

#Reciept to display quantity , movie and total,tax
 
def receipt():
    Name_Cinema = "Stark"
    import datetime
    t_date = datetime.datetime.now()
    Date_t = t_date.date()
    Tim_e = t_date.time()
    
    Ticket_Type = "Standard"
    #Additional_Cost = "G"

    edge = "+"                      
    border = "-"
    space = " "

    def border():
        print ("+" + "-"*52 + "+")

    border()
    print (space*25 +"RECIEPT")
    border()

    elements_1 = ["Movie","Date","Time"]     #Creating section 1

    for i in (elements_1):
        if (i == "Movie"):
            k = Movie_Name
        elif ( i == "Date"):
            k = Date_t
        else:
            k = Tim_e
        print (space*4 + i + ":"+space," ", k )

    border()

    elements_2 = ["Ticket Type","Quantity"] #Creating section 2

    print( space*2 + "Purchases" + space*9 + ":" + space*10 + "Payment(AED)")
    
    for i in (elements_2):
        if (i == "Ticket Type"):
            w = Ticket_Type
            a = space*12
            b = space*7
        elif (i == "Quantity"):
            w = Ticket_Quantity
            a = space*15
            b = space*10
        print(space*2 + i + str(b) + ":"+ str(a) + str(w))

    border()
    
    if CODE == "YES":
        print(space*2 + "Discounted Total" + space*2 +":"+ space*13+str(TotalCostDisc)+" AED")
    else:
        print(space*2 + "Total" + space*13+":"+ space*13+str(TotalCostDisc)+" AED")

    border()
    print( space*2 + "Thank you for visiting"+space+Name_Cinema+space+"Cinemas !")
    border()
    print(" ")
    print("-----END OF PROGRAM-----")
    print(" ")

#-----------------The final code to be run---------------------------

mainrun = "yes"
run = "yes"
while True:
    PASSWORD = input("Enter password to enter the program: ")
    if PASSWORD == "CBSE2019":
        while mainrun == "yes":
            try:
                while run == "yes":
                    init_menu() # first thing the users are shown
                    mydb.close()
            except:
                print("Sorry the program ran into a problem")
                print("The program is restarting")
                print("Sorry for the inconvenience")
                print(" ")
    if run != "yes" :
        break
