# sign up or login of theater management system program

import mysql.connector as conn
db=conn.connect(host='localhost',user='root',password='tiger123',db='Theatre') #Change password and database as you need to
cur=db.cursor()

#Table Creation 
def createTableCustomer():
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre")
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists Customer")
    mycursor.execute("create table customer(\
    Username varchar(50) primary key,\
    First_name varchar(100),\
    Second_name varchar(100),\
    last_name varchar(100),\
    DOB date,\
    Mobile_num varchar(15),\
    Gender varchar(1),  \
    Email_id varchar(100),\
    password varchar(50),\
    register_date datetime\
    );")
    mydb.commit()

def createTableGuestCustomer():
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre")
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists Guest_Customer")
    mycursor.execute("create table guest_customer(\
    Serial_number int(10) Primary key,\
    First_name varchar(100),\
    last_name varchar(100),\
    Mobile_num varchar(15), \
    login_date datetime\
    );")
    mydb.commit()

createTableCustomer()
createTableGuestCustomer() #Actual table Creation

#main execution process function

def init_menu():
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
    user_id = input("Enter your username: ")
    
    count = cur.execute("select count(*) from customer where username =  '"+user_id+"'")
    l_count = cur.fetchone()
    if l_count[0] >0:
        password = input("Enter yout password: ")
        p = cur.execute("select password from customer where username = '"+user_id+"'")
        l_count = cur.fetchone()
        if l_count[0]==password:
                ticket_booking() #change according to need

        else:
                print( "Incorrect username/password. ")
                print( "Try again. ")
                login_process()
    else:
           print(" Given username was not registered. ")
           init_menu()
                    


#Registration
        
def registration_process( ):

       user_id = input("Enter your username :")
       count = cur.execute("select count(*) from customer where username = '"+user_id+"'")
       l_count = cur.fetchone()
       
       if l_count[0]<= 0:   
       
                print( " * Required Field(s)")
                Fname=input("Enter your First Name* :  ")
                Sname=input("Enter your Second Name : ")
                Lname=input("Enter your Last Name*  : ")
                DOB=input("Enter your date of birth (Enter in (DD-MM-YYYY) format ) * : ")
                phonenum=input("Enter your moblie number : ")
                gen=input("Enter your Gender(M/F)* : ")
                email=input("Enter your email id  : ")

                i = 1
                while i <= 3 :
                    passwd = input("Enter password : ")
                    cpasswd = input("Confirm your password. : ")
                    if passwd != cpasswd  :
                        print ("Wrong Password . Try again.")
                        i=i+1
                    else :
                        break
                if i <= 3 :
                    cur.execute(" insert into customer values ('"+user_id+"','"+Fname+"', '"+Sname+"','"+Lname+"','"+DOB+"' ,'" +phonenum+"','"+gen+"','" +email+"','"+passwd+"' ,now())")
                    db.commit()
                    print(" Registration process was successful. ")
                    print(" please login to continue. ")
                    login_process()
       else:
              print(" Username is already taken ")
              registration_process()



# guest_Login

def  guest_login_process():
                   Fname=input("Enter your firstname*  : ")
                   Lname=input("Enter your lastname*  : ")
                   phonenum=input("Enter your moblie number : ")
                   cur.execute("select max(serial_number) from guest_customer ")
                   l_max = cur.fetchone()
                   if l_max[0] is None :
                       max_num=1
                   else:
                        max_num=l_max[0] + 1
                   cur.execute("insert into guest_customer values ("+str(max_num)+ ",'"+Fname+"','"+Lname+"','"+phonenum+"',now())")
                   db.commit()
                   ticket_booking()  # change according to need
                    
def ticket_booking():
     #sdad
     print("")
     
db.close()

