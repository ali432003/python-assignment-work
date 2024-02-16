
# #pyramid
# n = 5
# for j in range(n):
#     for i in range(n-j-1):
#        print(end=" ")
#     for k in range(j+1):
#         print("*",end=" ")
#     print()








   
# # n = 5
# #Right-sided traingle
# rows = 11
# for i in range(1,rows,2):
#         print('* '*i)
n = 5
for i in range(n-1):
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()       







