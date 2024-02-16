# camel case: camelCase mtlb alag krnee ke liye capital se likhtey e.g iPhone/i phone, eBay
# snake case: snake_case mtlb alag krnee ke liye "_" se likhtey e.g first_name,last_name 

# user = input("Enter any word or sentence:  ")
# choice = input("For snake_case press 'sc' and camelCase press 'cc':  ")
name_convert=""
# if choice=="sc":
#     print("snake case: ",end="")
#     for i in user:
#         if i.islower():
#             print(i, end="")
#         else:
#             print("_" + i.lower(), end="")    
# print("")

# if choice =="cc":
user = "kuch bhi"
c=user[0].lower() 
name_convert+=c
n=None
for i in user[1:]:
     if i==" ":
        n=" "
        pass
     else:
        if n==" ":
            i=i.upper()
        name_convert+=i
        n=None
print("camelCase: ",name_convert)