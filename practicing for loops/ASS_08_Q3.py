  
l1 = ['hockey','football','tennis','badminton','volleyball','cricket','squash','kabaddi','tennis']
a=1
for x in l1:
    print(x)

while True:
    b=input("do want to remove (y/n): ")
    if b=="y":
        a = input('enter a sport you want to remove: ')
    else:
        break
        
    while a not in l1: 
        a = input('The sport is not in the list kindly enter sport from the list: ')

    while  a in l1:
        l1.remove(a)

print(l1)


