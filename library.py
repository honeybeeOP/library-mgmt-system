import submit,ls,borrow,dateandtime
def main():
    while(True):
        #printing the task for library
        print("""
------------------- Library Manager --------------------
    
         Press 1 to Display Books
         Press 2 to borrow book
         Press 3 to return book
         Press 4 to exit
            """)
        try:
            #taking input for choices from user.
            choice = int(input ("   Press Task No: "))
            print(">-------------------------------------------------<")
            if(choice == 1):
                #opening books.txt file to read.
                displaybookfile = open("books.txt","r")
                print(displaybookfile.read())
                displaybookfile.close()
           
            elif(choice == 2):
                #calling ls and issuebook functions
                ls.ls()
                borrow.issuebook()
            
            elif(choice == 3):
                #calling ls and returnbook functions
                ls.ls()
                submit.returnbook()
            
            elif(choice == 4):
                #exiting the program.
                print("\n\n Thank You for using Library.\n\n")
                exit()
            
            else:
                print("wrong choice.....")
        except ValueError:
            print("You were supposed to input the suggested values. ")
def pswd():
    #asking password to accesss main().
    print("Please enter the password." "(library123)")
    password = input(" Enter the password: ")
    if password == "library123":
        main()
    else :
        print("wrong password")
        pswd()
pswd()
        

    
        
    
    
    
            
                
