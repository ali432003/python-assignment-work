#=========================TASK:03==========================#
a=int(input("Total price of the bill:"))
b=int(input("Total number of diners:"))
c=a//b

for i in range(1,b+1):
    print(f'share of {i} person: ',c)



