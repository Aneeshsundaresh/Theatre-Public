# sign up or login of theater management system program

import mysql.connector as conn
mydb = conn.connect(host="localhost",user="root",password="tiger123")
mycursor = mydb.cursor()


def createTableCustomer():
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre")
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists customer")
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
    
    ''' +---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| Username      | varchar(50)  | NO   | PRI | NULL    |       |
| First_name    | varchar(100) | YES  |     | NULL    |       |
| Second_name   | varchar(100) | YES  |     | NULL    |       |
| last_name     | varchar(100) | YES  |     | NULL    |       |
| DOB           | date         | YES  |     | NULL    |       |
| Mobile_num    | varchar(15)  | YES  |     | NULL    |       |
| Gender        | varchar(1)   | YES  |     | NULL    |       |
| Email_id      | varchar(100) | YES  |     | NULL    |       |
| password      | varchar(50)  | YES  |     | NULL    |       |
| register_date | datetime     | YES  |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+'''
    

def createTableGuestCustomer():
    mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre")
    mycursor = mydb.cursor()
    mycursor.execute("Drop table if exists guest_customer")
    mycursor.execute("create table guest_customer(\
    Serial_number int(10) Primary key,\
    First_name varchar(100),\
    last_name varchar(100),\
    Mobile_num varchar(15), \
    login_date datetime\
    );")
    mydb.commit()
    
'''+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| Serial_number | int(10)      | NO   | PRI | NULL    |       |
| First_name    | varchar(100) | YES  |     | NULL    |       |
| last_name     | varchar(100) | YES  |     | NULL    |       |
| Mobile_num    | varchar(15)  | YES  |     | NULL    |       |
| login_date    | datetime     | YES  |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+'''


createTableCustomer()
createTableGuestCustomer() #Actuall table creation

# create a table with following parameters to store info
''' create table customer(
    Username varchar(50) primary key,
    First_name varchar(100),
    Second_name varchar(100),
    last_name varchar(100),
    DOB date,
    Mobile_num varchar(15),
    Gender varchar(1),  
    Email_id varchar(100),
    password varchar(50),
    register_date datetime
    );
'''
''' you can use following to check for movie eligibility
mycursor.execute(" update Theater set Age=((select year(curdate())) - (select year(DOB) where Mobile_num=phonenum)) ")'''

'''create table guest_customer(
    Serial_number int(10) Primary key,
    First_name varchar(100),
    last_name varchar(100),
    Mobile_num varchar(15), 
    login_date datetime
    );
'''


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
    
    count = mycursor.execute("select count(*) from customer where username =  '"+user_id+"'")
    l_count = mycursor.fetchone()
    if l_count[0] >0:
        password = input("Enter yout password: ")
        p = mycuror.execute("select password from customer where username = '"+user_id+"'")
        l_count = mycursor.fetchone()
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
       count = mycursor.execute("select count(*) from customer where username = '"+user_id+"'")
       l_count = mycursor.fetchone()
       
       if l_count[0]<= 0:   
       
                print( " * Required Field(s)")
                Fname=input("Enter your First Name* :  ")
                Sname=input("Enter your Second Name : ")
                Lname=input("Enter your Last Name*  : ")
                DOB=input("Enter your date of birth (Enter in (YYYY-MM-DD) format ) * : ")
                phonenum=input("Enter your moblie number : ")
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
                    mycursor.execute(" insert into customer values ('"+user_id+"','"+Fname+"', '"+Sname+"','"+Lname+"','"+DOB+"' \
                    ,'" +phonenum+"','"+gen+"','" +email+"','"+passwd+"' ,now())")
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
                   mycursor.execute("select max(serial_number) from guest_customer ")
                   l_max = mycursor.fetchone()
                   if l_max[0] is None :
                       max_num=1
                   else:
                        max_num=l_max[0] + 1
                   mycursor.execute("insert into guest_customer values ("+str(max_num)+ ",'"+Fname+"','"+Lname+"','"+phonenum+"',now())")
                   db.commit()
                   ticket_booking()  # change according to need
                    
def ticket_booking():
     #sdad
     print("")
     
mydb.close()


