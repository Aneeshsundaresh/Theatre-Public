import mysql.connector as conn

username=input("enter username")
mydb = conn.connect(host="localhost",user="root",password="tiger123",\
                        database="Theatre")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE timings (name char(50),timing1 char(12), timing2 char(12), timing3 char(12), timing4 char(12), timing5 char(12), timing6 char(12), timing7 char(12))")


# The main program to Add, Delete or Display the movies.
def menu():
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
               if (choice==2):
                    delmovie()
               if (choice==3):
                    dispmovie()
               elif (choice==4):
                    print ("Exiting")
                    break
               else:
                    break
               
          else: #When the user is not an admin
               
               print("1. Display Movies and Timings")
               print("2. Book Tickets")
               print("3. Exit")
               choice=int(input("Enter your Choice"))
               if (choice==1):
                   dispmovies()
               elif (choice==2):
                    bookmovie()
               elif (choice==3):
                    print("Thank You")
                    break
               else:
                    break
                    c=input("Do you want to continue[yes or no]:")
                    
#For Admin
def addmovie():
     m=input("Enter the movies name:")
     t1=input("enter timing1 :")
     t2=input("enter timing2 :")
     t3=input("enter timing3 :")
     t4=input("enter timing4 :")
     t5=input("enter timing5 :")
     t6=input("enter timing6 :")
     t7=input("enter timing7 :")
     sql_insert_query =""" INSERT INTO timings (name,timing1,timing2,timing3,timing4,timing5,timing6,timing7) \
     VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
     
     insert_tuple=(m,t1,t2,t3,t4,t5,t6,t7)
     mycursor.execute(sql_insert_query, insert_tuple)
     print("Movies added")
     mydb.commit()
     
def delmovie():
     m=input("Enter the movies name:")
     mycursor.execute("DELETE FROM timings WHERE name=%s",(m,))
     mydb.commit()
     
     
#For User
def dispmovie():
     mycursor.execute("SELECT * from timings")
     myrecords=mycursor.fetchall()
     for x in myrecords:
          print (x)
          
def bookmovie():
     m=input("Name of the movie:")
     time=input("Timing:")
     # Print Reciept
     
menu()


