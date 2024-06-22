#Reciept to display quantity , movie and total,tax
 

Movie_Name = "X"
Date_t = "Y"
Tim_e= "Z"
Name_Cinema = "ABC"
Ticket_Type = "O"
Ticket_Quantity = "P"
Additional_Cost = "G"
Total_Cost = "EE"


edge = "+"                      
border = "-"
space = " "

def border():
    print ("+" + "-"*50 + "+")

border()
print (space*25 +"RECIEPT")
border()

elements_1 = ["Movie","Date","Time"]              #Creating section 1

for i in (elements_1):
    if (i == "Movie"):
        k = Movie_Name
    elif ( i == "Date"):
        k = Date_t
    else:
        k = Tim_e
    print (space*4 + i + ":"+space +k )

border()

elements_2 = ["Ticket Type","Quantity","Extras (food, drinks,etc.)"]   #Creating section 2

print( space*2 + "Purchases" + space*11 + "¦" + space*12 + "Payment(AED)")

for i in (elements_2):
    if (i == "Ticket Type"):
        w = Ticket_Type
        a = space*25
        b = space*4
    elif (i == "Quantity"):
        w = Ticket_Quantity
        a = space*25
        b = space*10
    else:
        w = Additional_Cost
        a = space*4
        b = space*5
    print(space*2 + i + b + ":"+ a + w)

border()

print(space*4 + "Total" + space*16 +":"+ space*21+Total_Cost)

border()

print( space*2 + "Thank you for visiting"+space+Name_Cinema+space+"Cinemas !")

border()



