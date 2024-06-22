import mysql.connector as connector
# To create a database to store movies
username=input("enter username")
db=connector.connect(host="127.0.0.1",user="root",passwd="password",database="movies")
mycur=db.cursor()

# The main program to Add, Delete or Display the movies.
def menu():
     c='yes'
     while (c=='yes'):
          if (username=='admin'):
               print("1) Add Movie")
               print("2) Delete Movie")
               print("3) Display Movies")
               print("4) Exit")
               choice=int(input("Enter your Choice"))
               if (choice==1):
                    addmovie()  # Will add Movie to thetable
               if (choice==2):
                    delmovie() # Will delete the movie from the table
               if (choice==3):
                    dispmovie() # Will display the movie
               elif (choice==4):
                    print ("Exiting")
                    break
               else:
                    c=input("Do you want to continue[yes or no]:")
          else:     
               print("1)Display Movies and Timings")
               print("2)Exit")
               choice=int(input("Enter your Choice"))
               if (choice==1):
                   dispmovie()
                   bookmovie()
               elif (choice==2):
                    print("Thank You")
                    break
               else:
                    c=input("Do you want to continue[yes or no]:")
def addmovie():    
     m=input("Enter the movies name:")
     t1=input("enter timing1 :")
     t2=input("enter timing2 :")
     t3=input("enter timing3 :")
     t4=input("enter timing4 :")
     t5=input("enter timing5 :")
     t6=input("enter timing6 :")
     t7=input("enter timing7 :")
     sql_insert_query =""" INSERT INTO timings (name,timings1,timings2,timings3,timings4,timings5,timings6,timings7) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
     insert_tuple=(m,t1,t2,t3,t4,t5,t6,t7)
     mycur.execute(sql_insert_query, insert_tuple)
     print("Movies added")
     db.commit()
def delmovie():
     m=input("Enter the movies name:")
     mycur.execute("DELETE FROM timings WHERE name=%s",(m,))
     db.commit()
def dispmovie():
     mycur.execute("SELECT * from timings")
     myrecords=mycur.fetchall()
     for x in myrecords:
          print (x)
def bookmovie():
     m=input("Name of the movie:")
     time=input("Timing:")
     # Print Reciept
     
menu()
