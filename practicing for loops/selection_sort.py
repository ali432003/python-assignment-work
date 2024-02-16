# # Selection sort in Python

# def sort(data):
#     for i in range(len(data)-1):  #n-1, where n is total items in list
#         minposition = i
#         for j in range(i,len(data)): #
#             if data[j] < data[minposition]:
#                 minposition = j
        
        
#         temp = data[i]
#         data[i] = data[minposition]
#         data[minposition] = temp
      
 

# data = [16,-2, 45, 0, 11]
# print("unsorted: ",data)
# sort(data)
# print("sorted: ",data)


#Linear-Searching

# a = [15,17,8,0,5,3,12,18]
# print(a)
# user = int(input("search: ")) 

# for i in range(len(a)):
#     if a[i]==user:
#         print(user," is present at  index",i)
#         print(f"position of {user} is",i+1)
#         break
# else:
#     print(f"{user} is not present")

#Binary-Searching


# def binary_search(lst,item):
#     first_index = 0
#     end_index = len(lst)-1
    
#     while first_index<=end_index:
#         mid = first_index+(end_index-first_index)//2
#         mid = lst[mid]
#         if lst[mid]==item:
#             return item
#         elif lst[mid]<item:
#            mid = end_index-1
#         else:
#             mid = first_index+1
#     return none       

# lst_a = [1,2,3,4,5,6,7,12,15]
# item_a = 12

# print(binary_search(lst_a,item_a)) 



# rock paper scisssor


# user1_action = input("Enter a choice (rock, paper, scissors): ")
# user2_action = input("Enter a choice (rock, paper, scissors): ")

# print(f"\nplayer 1 {user1_action}, player 2 {user2_action}.\n")

# if user1_action == user2_action:
#     print(f"Both players selected {user1_action}. It's a tie!")
# elif user1_action == "rock":
#     if user2_action == "scissors":
#         print("Rock smashes scissors! player 1 wins!")
#     else:
#         print("Paper covers rock! player 2 wins!.")
# elif user1_action == "paper":
#     if user2_action == "rock":
#         print("Paper covers rock! player 1 wins!")
#     else:
#         print("Scissors cuts paper! player 2 wins!")
# elif user1_action == "scissors":
#     if user2_action == "paper":
#         print("Scissors cuts paper! player 1 wins!")
#     else:
#         print("Rock smashes scissors! player 2 wins!")


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
# from msvcrt import kbhit

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

# def simpleArraySum(ar):
#     # Write your code here
#     arr=[]
#     for i in range(len(arr)):
#         arr[i]+=i

# arr = [1,2,3,4,5,7,8]
# print(simpleArraySum(arr))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = simpleArraySum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    for i in len(arr):
        if arr[i]==n:
            print(n)