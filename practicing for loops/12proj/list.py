# Exercise 1: Reverse a list in Python
# Given:
# list1 = [100, 200, 300, 400, 500]
# Expected output:
# [500, 400, 300, 200, 100]

list1 = [100, 200, 300, 400, 500]

rev = list1[::-1]
print(list1)
print(rev)

# Exercise 2: Turn every item of a list into its square
# Given a list of numbers. Write a program to turn every item of a list into its square.
# Given:
# Numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output:
# [1, 4, 9, 16, 25, 36, 49]


Numbers = [1, 2, 3, 4, 5, 6, 7]
sqr = []
for i in Numbers:
    i *= i
    sqr.append(i)

print(Numbers)
print(sqr)

# Exercise 3: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

out = list1[0]+list2[0],list1[0]+list2[1],list1[1]+list2[0],list1[1]+list2[1]
print(list1,list2)
print(list(out))

# Exercise 4: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order
# and items from list2 in reverse order.
# Given
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

print(list1,list2)
for (items1,items2) in zip(list1,list2[::-1]):
    print(items1,items2)

# Exercise 5: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
# Given:
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:
# [5, 15, 25, 50]    

l = [5, 20, 15, 20, 25, 50, 20]
rem = 20

print(l)
while rem in l:
    l.remove(rem)

print(l)    