import math
import os
import random
import re
import sys

'''n = int(input("enter a number: "))
if (n % 2)!=0:
    print("Weird")
elif (n % 2)==0 in range(2,5):
    print("Not Weird")
elif (n % 2)==0 in range(6,20):
    print("Weird")
elif (n % 2)==0>20:
    print("Not Weird")'''      



n = int(input("enter a number:"))
if n % 2:
 print("Weird")
elif 2 <= n <= 5:
 print("Not Weird")
elif 6 <= n <= 20:
 print("Weird")
elif n % 2 or n>20:
 print("Not Weird")    
else:
 print("Not Weird")   
  
 