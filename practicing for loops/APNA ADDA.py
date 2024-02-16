n = 5
# increasing traingle by 1
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# # inverted pyramid
# # increasing triangle
# for i in range(n-1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# Decreasing triangle
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()       



# increasing triangle by *2
# rows = 11
# for i in range(1,rows,2):
#     print("* "*i)
# n = int(input("enter: "))
# m = 0
# a = 65
# #pyramid
# for i in range(n):
#     for j in range(n-i-1):
#         print(end=" ")
#     for k in range(i+1): # increasing
#         print(k+m,end=" ") #C
#     a+=k+1
#     print()    


# Diamond# 
# Hill - pattern
for i in range(n-1):
    for j in range(i,n): #decreasing
        print(' ',end='')
    for j in range(i):    
        print('*',end='')
    for k in range(i+1): #increasing
        print('*',end='')
    print()       

#inverted hill-pattern
for i in range(n):
    for j in range(i+1): #increasing
        print(' ',end='')
    for j in range(i,n-1):    
        print('-',end='')
    for k in range(i,n): #decreasing
        print('-',end='')
    print()       


# #decreasing-pyramid
# for i in range(n, 0, -1):
#     for j in range(0, n - i):
#         print(end = ' ')
#     for k in range(0, i):
#         print(k+1, end = ' ')
#     #n+=k+1    
#     print()       
#increasing-pyramid
# for i in range(n):
#     for j in range(n-i-1):
#         print(end="  ")
#     for k in range(i+1):
#         print(k+1,end=" ")
#     #n+=k+1    
#     print()    


#palinormal (wo number jiska ulta=seedha)
# m = list(input('enter: '))

# m1=list(m)
# m1.reverse()

# if m1==m:
#     print("its palinormal")
# else:
#     print("no palinormal")


# d = lambda a: a
# num = int(input())
# # num2 = int(input())

# print(d(num))

# from cmath import e
# from re import I


# user = input("enter: ")
# a = 0
# e = 0
# i = 0
# o = 0
# u = 0

# for letter in user:
#     if letter == "a":
#         a+=1
#     elif letter =="e":
#         e+=1
#     elif letter =="i":
#         i+=1
#     elif letter =="o":
#         o+=1
#     elif letter == "u":
#         u+=1    

# print("freq a",a)
# print("freq e",e)
# print("freq i",i)
# print("freq o",o)
# print("freQ u",u)

# from unicodedata import decimal


# # user = int(input())

# # convert = (user)
# # print(convert)

# def palindrome(m):
#     # m1=list(m)
#     # m1.reverse()
#     m1 = m[::-1]
#     if m1==m: 
#      print("its palindrome")
#     else:
#      print("no palindrome")

# user = list(input("enter: "))
# palindrome(user)

# # m = list(input('enter: '))

# # m1=list(m)
# # m1.reverse()

# # if m1==m:
#     return palin 
# #     print("its palinormal")
# # else:
# #     print("no palinormal")

# def is_palindrome(s):
#     if len(s) < 1:  # ye 1 number ya 1 string ko janey nhi dega iss loop se
#         return True
#     else:
#         if s[0] == s[-1]:
#             return is_palindrome(s[1:-1])
#         else:
#             return False
# a=str(input("Enter string:"))
# if(is_palindrome(a)==True):
#     print("String is a palindrome!")
# else:
#     print("String isn't a palindrome!")


# f = lambda a,b: a+b

# num1 = int(input("enter"))
# num2 = int(input("dal dubara"))

# print(f(num1,num2))



# n=4
# a=65
# for i in range(n):
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(chr(a),end=" ")
#         a+=1
#     print()
# for i in range(n+1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print(chr(a),end=" ")
#         a+=1
#     print()

# # Diamond# 
# n = 5
# a = 65
# # Hill - pattern
# for i in range(n-1):
#     for j in range(i,n): #decreasing
#         print(' ',end='')
#     # for j in range(i):    
#         # print(j+1,end='')
#     for k in range(i+1): #increasing
#         print(k+1,end='')
#         a+=1
#     print()       

# #inverted hill-pattern
# for i in range(n):
#     for j in range(i+1): #increasing
#         print(' ',end='')
#     # for j in range(i,n-1):    
#         # print(j+1,end='')
#     for k in range(i,n): #decreasing
#         print(k+1,end='')
#         a+=1
#     print()       


# a = int(input("enter num 1: "))
# b = int(input("enter num 2: "))
# f = lambda x,y : x+y
# total = 0

# for i in range(a,b+1): #ye loop n-1 tk chlega
#     j = f(i,total) #dono ki value sath sath barheingi
#     total = j

# print("sum of all in between given numbers: ",j)

# #p = 65
# m = 0
# n = 5
 
# for i in range(n):
#     for j in range(i,n): #decreasing
#         print(' ',end=" ")
#     for k in range(i+1):
#         print(k+1,end=" ")
#         m += 1
#     print()    

# seedhaa
                                                         
# m = 0
# n = 5
# a = 65
# for i in range(n-1):
#     for j in range(i,n):
#         print(' ',end='')
#     for k in range(i+1):
#         print(k+m,end=" ") #changings
#     m+=k+1
#     print()        
# # ultaaa
# for i in range(n):
#     for j in range(i+1):
#         print(end=' ')
#     for k in range(i,n):
#         print(k+m,end=" ") #changings
#     m+=k+1 
#     print()            
             
# total = 0
# c = []
# a = int(input("enter: "))
# for i in range(1,a):
#     if a%i==0:
#         c.append(i)
# for i in c:
#     total+=i
# if total ==a:
#     print(a,"is perfect")
# else:
#     print(a,"not perfect")    


# lst=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U"
# ,"V"] 



# m = 0

# for i in range(4):
#     for j in range(i+1):
#         print(m+j,end=" ")
#     m+=j+1
#     print()

# m = 0
# for i in range(9):
#     for j in range(i,9):
#         print("*",end=" ")
#     m+=j+1
#     print()            
    
# for i in range(9):
#     for j in range(i,9):
#         print("*",end=" ")
#     m+j+1    
#     print()


# a = 0        
# for i in range(n-1):
#     for j in range(i+1):
#         print(k+a,end=" ")
#     a+=k+1
#     print()   

# for i in range(n):
#     for j in range(i,n):
#         print(k+a,end=" ")
#     a+=k+1
#     print()             

# from email.mime import audio


# num = input("enter a number or string: ")

# a = list(num)
# a = a[::-1]
# a = ' '.join(a)

# print(a)

#                               random_pass generator
# import random
# import string 

# user = int(input("enter the lenght of pass: "))

# symbols = '@!#$%&><\+*-/;?`'       
# b = string.ascii_letters+string.digits+string.capwords(symbols) 
# c = ''.join(random.choice(b)for i in range(user))

# print('pass: ',c)
    

#                                  listing Even/Odd

# numList1 = [17, 12, 25, 3, 36, 49, 28, 27,6,8]
# numList2 = [19, 40, 42 , 30, 15, 60, 75, 50]

# c1 = []

# for i in range(len(numList1)):
#     if numList1[i]%2==0:  #even condition
#         c1.append(numList1[i]) #can take all even from List1 and append it in c1
# for j in range(len(numList2)):
#     if numList2[j]%2!=0:  #odd condition
#         c1.append(numList2[j]) #can take all odd from List2 and append it in c2

# print(c1)

#                         Even Odd and prime counter
# import math
# s = [1,2,3,5,7,11,13,17]

# even = 0
# odd = 0
# prime = 0

# for i in range(len(s)):
#  if s[i]%2==0:
#     even+=1
#  if s[i]%2!=0:
#     odd+=1
# for i in range(2, int(math.sqrt(s[i])) + 1):
#                if(s[i] % i) == 0:
#                   prime+=1 
#                else:
#                   print(s[i]%i)

# print(s,'lenght: ',len(s))
# print('even',even)
# print('odd',odd)
# print('prime',prime)



# n = 5
# a = 65
# m = 0

# for i in range(n):
#     for j in range(i,n):
#         print(end=' ')
#     for k in range(i+1):    
#         print(chr(a),end=' ')
#         a+=1
#     print()

#                                  Armstrong number
# num = int(input())
# sum = 0

# temp = num
# while temp > 0:
#     digit = temp%10
#     sum  += digit**3
#     temp //= 10

# if sum == num:
#     print(num," hai")
# else:
#     print(num,'nhi ha')        

# n = 5
# a = 65
# for i in range(n-1):
#     for j in range(i+1):
#         print(chr(a),end=' ')
#     a+=1
#     print()    

# for i in range(n):
#     for j in range(i,n):
#         print(chr(a),end=' ')
#     a+=1
# #     print()    
# n = 8
# m = 0

# for i in range(n):
#     for j in range(i):
#         # print(end=' ')
#     # for j in range(i+1):
#         print(i,end=' ')
#         m+=i+1 
#     print()        

# a = list(input())
# a.reverse()

# b = [str(integer) for integer in a]
# a_string = ''.join(b)

# res = int(a_string)

# print(res)

# Ask user for any num,str,symbols etc
# user = list(input("Enter: "))
# # reversing list values
# user = user[::-1]
# # converting list values into string
# stri = [str(i) for i in user]
# # concatenating/joining list values to the string 
# stri = ''.join(stri)
# print
# print(stri)


# # > greater than
# # >= greater than or equals to
# # <  less than 
# # <= less than or equals to
# # == equals to comparing
# # != not equals to comparing

# name = input('what is your name ? ')

# # match name:
# #     case "ali"|'Ali'|'sara'|'ayesha'|'maryam':
# #         print("ADDRESS: Comander heights")
# #     case 'noman'|'xyz':
# #         print("ADRESS: Anda morr")    
# #     case _:
# #         print("idk")    


            
# txt= "kuchh bhii likh dein.."

# x = txt.split()

# #x=int(x)
# for i in x:
#  print(i)


# while True:
#     n = int(input("What's n? "))
#     if n < 10:
#         continue
#     else:
#         break
        

# name="bilalAhmed"
# name_convert=""
# c=name[0].lower()
# name_convert+=c
# for i in name[1:]:
#     if i in  "ABCDEFGHIJKLMOPQRSTUVWXYZ":
#         name_convert+="_"
#         i=i.lower()
#         name_convert+=i
#     else:
#         name_convert+=i
# print(name_convert)        

# name= input("En")
# name_convert=""
# c=name[0].lower()
# name_convert+=c
# n=None
# for i in name[1:]:
#     if i==" ":
#         n=" "
#         pass
#     else:
#         if n==" ":
#             i=i.upper()
#         name_convert+=i
#         n=None
# print(name_convert)

# a ="ali"
# print(a.upper()) #age var ko check krna ho kee upper ha ya lower bool me nas chahye ho toh hm loug isupper/lower use krtey 
# # agr var ko convert krnaa ho tohh .upper ya .lower use krteyy hn


# # m=0
# a = 65
# for i in range(4-1):
#     for j in range(i,4):
#         print(end="---")
#     for k in range(i+1):
#         print(".|.",end="   ")
#         # m+=1
#     print('     ')
    
# for i in range(4):
#     for j in range(i+1):
#         print(end='---')     
#     for k in range(i,4):
#         print(".|.",end='   ')   
#         # a+=1
#     print(' ')

# def minion_game(string):
#     string=string.lower()
#     player_1=0
#     player_2=0
#     vowels="aeiou"
#     for i in range(len(string)):
#         if string[i] in vowels:
#             player_1+= len(string)-i
#         else:
#             player_2+= len(string)-i    
    
#     if player_1>player_2:
#         print("Kevin",player_1)
#     elif player_1==player_2:
#         print("Draw")    
#     else:
#         print("Start",player_2)    


# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")
      

# def is_valid(s):
#  # vanity plates may contain a maximum of 6 characters (letters or numbers)
#     # and a minimum of 2 characters.
#     if len(s) < 2 or len(s) > 6:
#         return False

#     # All vanity plates must start with at least two letters
#     if s[0].isalpha() == False or s[1].isalpha() == False:
#         return False

#     # Numbers cannot be used in the middle of a plate; they must come at the end.
#     # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
#     # The first number used cannot be a ‘0’
#     i = 0
#     while i < len(s):
#         if s[i].isalpha() == False:
#             if s[i] == '0':
#                 return False
#             else:
#                 break
#         i += 1

#     for i in range(len(s)):
#         if s[i].isdigit():
#             if not s[i:].isdigit():
#                 return False

#     # No periods, spaces, or punctuation marks are allowed
#     for c in s:
#         if c in ['.', ' ', '!', '?']:
#             return False

#     # If we pass all the tests, return True
#     return True


# if __name__ == "__main__":
#     main()


# # rock paper scisssor

# r = 0
# p = 0
# s = 0

# user_1 = input("input: ")
# user_2 = input("input: ")

# if user_1==user_2:
#     print("draw")
# elif user_1=="r" or user_2=="p":
#     print("user 2 win")
#     p=p+1
# elif user_1=="s" or user_2=="p":  
#     print("user 1 win")
#     s=s+1
# elif user_1=="r" or user_2== "s":
#     print("user 1 win")
#     r=r+1


# # if __name__ == '__main__':
# # h = int(input())
# # arr = map(int, input().split())
# # for i in arr:
# #     if i in arr[i] > i:
# #         print(i)
                
