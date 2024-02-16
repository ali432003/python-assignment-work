list1 = [1,2,3,4,5,6,7,8]
list2 = ["a","b","c","d","e","f","g","h"]

while len(list1) < len(list2): 
    list1.append(" ")
while len(list1) > len(list2): 
    list1.append(" ")
list2.reverse()

# c=0
# d=0
for (i,j) in zip(list1,list2):
    print(i,j)