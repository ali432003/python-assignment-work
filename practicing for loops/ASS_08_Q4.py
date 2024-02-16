l1=[11,34,54,67,52,98,18,76,34,21,45,89]
l2 = [24,57,96,54,84,75,12,36,49,51,48,99.87,61,65,96,61]

print("list are:")
print("list1: ",l1)
print("list2: ",l2)

while len(l1) < len(l2): 
    l1.append(" ")
while len(l2) < len(l1): 
    l2.append(" ")
    
for i in l1:
    if i!=" ":
            if i%2!=0: 
               
                c=l1.index(i) 
                l2.insert(c,i)  
                l1[c]=" "

for i in l2:
    if i!=" ":
       if i%2==0: 
       
            c=l2.index(i)
            l1.insert(c,i)
            l2[c]=" "

while " " in l1:
    l1.remove(" ")
while " " in l2:
    l2.remove(" ")

print("swaped list are: ")
print("odd num series: ",l2) 
print("even num series: ",l1)















