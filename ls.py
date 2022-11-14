def ls():
    #initializing the given variable as global 
    global book_name
    global authorname
    global quantity
    global cost
    # creating list
    book_name=[]            
    authorname=[]
    quantity=[]
    cost=[]
    #opening books.txt file and spliting it.
    with open("books.txt","r") as file:
        
        lines = file.readlines()  
        lines = [x.strip('\n') for x in lines]
        for i in range(len(lines)):
            index = 0
            for a in lines[i].split(','): 
                if(index == 0):
                    book_name.append(a)
                elif(index == 1):
                    authorname.append(a)
                elif(index == 2):
                    quantity.append(a)
                elif(index == 3):
                    cost.append(a.strip("$"))
                index += 1
        
    
        
