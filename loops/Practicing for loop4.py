num = int(input("Enter the number of people you want to invite: "))

if num >= 10:
    print("Too many people")
else:
    for i in range(num):
        name = str(input("Enter the name of "+ str(i+1) +" person: "))
        print(name + " has been invited")
