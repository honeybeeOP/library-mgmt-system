import ls,dateandtime
def issuebook():
    success = False
    while(True):
        # asking user for their fullname.
        f_name=input("  Enter the first name of the borrower: ")
        if f_name.isalpha():
            break
        print("invalid name")
    while(True):
        l_name=input("  Enter the last name of the borrower: ")
        print(">------------------------------------------------<")
        print("\n  Now you can borrow books.")
        if l_name.isalpha():
            break
        print("invalid name")

    #creating a text file and writing the file as mentioned below.
    t="Borrowed-" +f_name+" "+ l_name + ".txt"
    with open(t,"w+") as f:
        f.write("                    Library               \n")
        f.write("-------------------------------------------------\n")
        f.write("       Borrowed By: "+ f_name+" "+l_name+"\n")
        f.write("  Date: " + dateandtime.Date()+"          Time:"+ dateandtime.Time()+"\n\n")
        f.write("S.N. \tBookname \t\tAuthorname  \t\t cost\n" )
        
    while success == False:
        print("\n SELECT THE BOOK YOU WANT TO ISSUE :")
        print("-----------------------------------")
        for i in range(len(ls.book_name)):
            print( i, "-" , ls.book_name[i])

        try:
            a = int(input("\nPress the index of the book you want to issue: "))
            try:
                if(int(ls.quantity[a])>0):
                    print(" [ Book available ]")
                    with open(t,"a") as file:
                        file.write("  1.\t"+ ls.book_name[a]+"\t\t"+ls.authorname[a]+ "\t\t$"+ ls.cost[a]+"\n")

                    ls.quantity[a]=int(ls.quantity[a])-1
                    with open("books.txt","w+") as file:
                        for i in range(10):
                            file.write(ls.book_name[i]+","+ls.authorname[i]+","+str(ls.quantity[i])+","+"$"+ls.cost[i]+"\n")

                    loop = True
                    count=1
                    while loop == True:
                        #asking user if they want to borrow multiple book.
                        choice = str(input("\nDo you want to borrow more books? Press y for yes and n for no."))
                        if(choice.lower()=="y"):
                            print ("\n YOU CAN NOW BORROW OTHER BOOKS. (NOTE:You cannot borrow same book.)")
                            count=count+1
                            print("\n SELECT THE BOOK YOU WANT TO ISSUE :")
                            print("-----------------------------------")
                            for i in range(len(ls.book_name)):
                                print(i," - ",ls.book_name[i])
                            a=int(input("\nPress the index of the book you want to issue: "))
                            if(int(ls.quantity[a])>0):
                                print(" [ Book available ] ")
                                #adding the book details to borrow.txt file 
                                with open(t,"a") as file:
                                    file.write("  " +str(count)+".\t"+ ls.book_name[a]+"\t\t"+ls.authorname[a]+"\t\t$" +ls.cost[a]+"\n")

                                #decreasing the quantity of the books after borrowing
                                ls.quantity[a]=int(ls.quantity[a])-1
                                #opening the file books.txt and updating it 
                                with open("books.txt","w+") as f:
                                    for i in range(10):
                                        f.write(ls.book_name[i]+","+ls.authorname[i]+","+str(ls.quantity[i])+","+"$"+ls.cost[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                            #when choice no is choosen then code for displaying thank you message.
                        elif (choice.lower()=="n"):
                            print ("\n\n          THANK YOU FOR BORROWING. ")
                            loop=False
                            success=True
                        else:
                            print("Please choose y for yes and n for no.")
                            
                else:
                    print("SORRY! BOOK NOT AVAILABLE")
                    issuebook()
                    success=False
            except IndexError:
                    print("\n Please choose book acording to their number.")
        except ValueError:
            print("\n Please choose as suggested.")

                    
            
