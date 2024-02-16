#OBJECT 3

list1 = ["maths","english","pst","urdu","islamiat","computer"]
for i in range(len(list1)):
   print(i+1,list1[i])
b = input("which subject you dont like: ")
list1.remove(b)
print(list1)   