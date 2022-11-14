import ls,dateandtime
def returnbook():
    success = False
    while(True):
        # asking user for their fullname.
        firstname=input("  Enter the first name of the borrower: ")
        if firstname.isalpha():
            break
        print("invalid name.")
    while(True):
        lastname=input("  Enter the last name of the borrower: ")
        print(">------------------------------------------------<")
        if lastname.isalpha():
            break
        print("invalid name.")
        
    #creating a text file and writing the file as mentioned below.    
    a="Borrowed-" +firstname+" "+ lastname + ".txt"
    try:
        with open(a,"r") as file:
            lines=file.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as file:
            data=file.read()
            print(data)
    except:
        print("No match found!")
        returnbook()
        
    #creating return.txt file and writing the file as mentioned below.
    b="Return-" +firstname+" "+ lastname + ".txt"
    with open(b,"w+")as f:
        f.write("                     library                   \n")
        f.write("--------------------------------------------------------\n" "      Returned By: " +firstname.upper()+ " " +lastname.upper()+ ".\n"  )  
        f.write("   Date: " + dateandtime.Date()+"              Time:"+ dateandtime.Time()+"\n")
        f.write("S.N.\tbook_name\t\t authorname\t\tCost\n")

    total_cost=0.0
    for i in range(10):
        if ls.book_name[i] in data:
            with open(b,"a") as f:
                f.write(" -.\t\t"+ls.book_name[i]+"\t\t"+ls.authorname[i]+"\t$"+ls.cost[i]+"\n")
                #increasing the quantity of the books after returning
                ls.quantity[i]=int(ls.quantity[i])+1
            total_cost+=float(ls.cost[i])
            
    print("                           total cost:"+"$"+str(total_cost))
    print("Is the book return date expired? press y for yes n for no.")
    choosed_option=input(" -->")
    if(choosed_option.lower()=="y"):
        print("how many days you are late to return?")
        #asking the borrower for the days he was late to return
        day=int(input("-->"))
        fine=3*day
       
    elif(choosed_option.lower()=="n"):
        fine=0.0
        #writing the fine to return.txt file 
    with open(b,"a")as file:
        file.write("\t\t\t\t\t\t\t\tFine: $"+ str(fine)+"\n")
    final_cost=total_cost+fine

    print("Final cost: " "$"+str(final_cost))
    print ("\n\n Thank you for returning. ")
    #writing the Total cost to return.txt file 
    with open(b,"a")as f:
        f.write("\t\t\t\t\t\t\t\tTotal cost: $"+ str(total_cost))
    
        
    with open("books.txt","w+") as f:
            for i in range(10):
                f.write(ls.book_name[i]+","+ls.authorname[i]+","+str(ls.quantity[i])+","+"$"+ls.cost[i]+"\n")

