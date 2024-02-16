#####COMPREHENSIONS####

#list-comprehensions 

# list_1 = [i for i in range(100) if i%4==0]
# print(list_1)

#dictionary-comprehensions
dic1_1 = {i:f"item{i}" for i in range(5)}
print(dic1_1)
dic1_1 = {value:key for key,value in dic1_1.items()}
print(dic1_1)

#set-comprehensions


n = int(input("How many items do you want to add to your inventory: "))
i = 0
l = []
while(i<n):
    a = input("Enter the item: ")
    l.append(a)
    i += 1

choice = int(input("Press '1' for generating a list comprehension\nPress '2' for generating a set comprehension\nPress '3' for generating a generator comprehension: "))

if choice == 1:
    list = [item for item in l]
    print(list)

elif choice == 2:
    set = {item for item in l}
    print(set)

elif choice == 3:
    gen = (item for item in l)
    for c in gen:
        print(c)
