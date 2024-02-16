# mydict = {
#     "marks":[1,2,3],
#     "mks1":"24",
#     "m2":{"marks":"1,2,3"},
#     "name":"ali",
#     1 : 2    
# }

# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())

# up = {
#     "snakes":"freind",
#     "Joy":"maza ana",
#     "m2":'1,5,8'
# }

# mydict.update(up)

# print(mydict)


# a = {1,2,3,4} 
# b = set()
# print(type(a),type(b))
# print(a) , print(b)
# a.add(7) , b.add(2)
# a.add(9) , b.add(5)
# a.add((10,11)) , b.add(10)
# print(a) , print(b)


# from codecs import ascii_encode
# from string import ascii_uppercase


# # name = input('enter your name: ')
# # vowels = ("aeiou")

# # for i in vowels:
# #     name  =  name.replace(i,"")

# # print(name.upper())


# vanity_plate = input("enter:")

# upper_case = ascii_uppercase
# num = [0,1,2,3,4,5,6,7,8,9]


# if vanity_plate in [" ", '?',"!","."]:
#     print("SYNTAX ERROR,invalid")      

# elif len(vanity_plate)>6 or len(vanity_plate)<2:
#     print("LENGTH ERROR,invalid")
# elif vanity_plate[0]==num or vanity_plate[1]==num:
#     print("ERROR first 2 is always letters,invalid")
# elif vanity_plate[-1]==upper_case or vanity_plate[-2]==upper_case:
#     print("ERROR last 2 is always num,invalid") 
# else:
#     print("Valid")    
    


# print(  "\tO  O \n"
#           "\t|\n"
#           "\tM\n"
#         "\t_| |_\n"
#        "\t/     \ \n"
#        "\t|     |\n"
#      "\t( . ) ( . )\n"
#      "     "


# )
# my_list = ['p',['r',['o','e'],'b'],'l','e','m']

# my_list[1][1].remove('o')
# print(my_list)

# l = [3, 8, 1, 6, 8, 8, 4, 'a']
# print(l.count(6))

# states = [
#   'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia',
#   'Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts'
#   ,'Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New'
#   'Jersey','New Mexico','New York','North Carolina','North'
#   'Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South'
#   'Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West'
#   'Virginia','Wisconsin','Wyoming', 'Europe' ]

# for x in states:
#   if x[0]=='A'or x[0]=='E' or x[0]=='I'or x[0]=="O" or x[0]=='U':
#     print(x,end=", ")

# n=int(input("Enter the number of terms: "))
# sum1=0
# for i in range(1,n+1):
#  sum1=sum1+(1/i)
# print("The sum of series is",round(sum1,2))


# from ctypes import Union


# l1 = []

# l1_size = int(input('enter list_1 size: '))

# for i in range(l1_size):
#     num = int(input("enter a number:  "))
#     l1.append(num)

# l2 = []
# l2_size = int(input('enter list_2 size: '))

# for i in range(l2_size):
#     num2 = int(input("enter a number:  "))
#     l2.append(num2)

# print("l1: ",l1)
# print("l2: ",l2)

# union = list(set().i(l1,l2))
# print("union: ",union)



# employees = [
#  {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
#  {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
#  {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
#  {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
# ]

# def get_name(employee):
#     return employee.get('Name')

# get_name(employees)    

# def percentage(obt_num,total_num):
#     p = (obt_num/total_num)*100
#     return p

# obt = int(input('enter obtained num: '))
# tot = int(input('enter total num: '))


# print(round(percentage(obt,tot)),'%')

# def greet(n):
#     print("Have a good day sir, ",n)

# name = input("enter your name: ")
# greet(name)

# def sumed(num1,num2=''):
#     return num1 + num2
#     if sumed(num1,num2)==sumed():
#         print(0)


# sumed()
# s = sumed(5,5)
# print(s)

# def dash(n):
#     odd=False
#     list_of_all=[]
#     for i in n:
#         i=int(i)
#         if i%2!=0:
#             if odd==True:
                
#                 list_of_all.append("-")
#                 list_of_all.append(str(i))
                
#             else:
#                 list_of_all.append(str(i))
#                 odd=True
#         else:
#             list_of_all.append(str(i))
#             odd=False
            
#     print("".join(list_of_all))
# dash("56730")
       
        

# n = str(99946)
# for even in n:
#     if int(even)%2==0:
#         e = even


# req = print(dash(n),end="-")
# req1 = e.join(req)
# print(req1)


# def insertion_sort(seq):
#     seq_indexing = range(1,len(seq)) #cuz there is no item on the left_side of 1st
#     for i in seq_indexing:
#         items_to_sort = seq[i]
#         while seq[i-1] > items_to_sort and i>0:  #i>0 cuz py doesn't allow negative indexing
#             #swaping
#             seq[i],seq[i-1] = seq[i-1],seq[i]
#             i = i-1 #for next item in array
#     return seq        

# print(insertion_sort([4,5,6,1,9,10,15,19,3,20]))

# a = [4,5,6,1,9,10,15.5]


import random

arr = [0,1,2,3,4,5,6,7,8,9]

n=random.sample(arr,len(arr))

print(n)
# k = 6

# for i in range(len(a)):
#     mid = a[0]+a[:-1]/2
#     while i>0:
#         if k>mid:
#             a[:-1]==k
#             print(i)
#         elif k<mid:
#             a[0]==k
#             print(i)   
#     else:
#         print(i)     
# 
# pyt_list = []

# for _ in range(int(input())):
#         name = input("name: ")
#         score = float(input("score: "))
#         pyt_list.append([name,score]) 
#         sorted_score = sorted(list(set([x[1] for x in pyt_list])))
# s = sorted_score[1]
# l = []
# for stu in pyt_list:
#     if s==stu[1]:
#         l.append(stu[0])

# for stu in sorted(l):
#     print(stu)

# print(pyt_list)
# score = str(score)
# for i in score:
#     print(i)



# print("YOUR PHONE BOOK")

                                                               

# name = input("enter name: ") 
# num = int(input("enter his/her number: "))

# phone_book = []
# phone_book.append([name,num])
# again = input("want to add another num? press y or n: ")
# while again > 0:
#     again = input("want to add another num? press y or n: ")
#     name = input("enter name: ") 
#     num = int(input("enter his/her number: "))
#     phone_book.append([name,num])
#     if again=='y':
#         continue
#     else:
#         break
    

# edit = input("Do you want to edit your phone book? for yes(y) & No(n): ")
# if edit == "y":
#     name_to_rem = input("enter name to remove: ")
#     phone_book.remove(name_to_rem)
# else:
#     print(phone_book)
