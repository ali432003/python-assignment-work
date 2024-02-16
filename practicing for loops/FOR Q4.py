a = int(input("Enter the number of people you want to invite: "))
x = []
if a >= 10:
    print("Too many people")
else:
    for i in range(a):
        b = str(input("Enter the name of "+ str(i+1) +" person: "))
        # x.append(b)
        print(b + " has been invited")
        x.append(b)
    
    print("\t\tlist of  people invited:\t\t")
    for i in range(len(x)):
        print(i+1,x[i])


        

        
