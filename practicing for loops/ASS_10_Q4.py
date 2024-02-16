
# def divisors(integer):
#     for i in range(1, integer+1):
#         if divisors(integer) % i == 0:
#             print(i)


# integer = int(input("Please enter any integer to find divisors: "))

# print("divisors are: ")
# divisors(integer)



def divisors(x,i):
    if i==0:
        return 
    if x%i == 0:
        print(i)
    return divisors (x,i-1) 

user = int(input("Please enter any integer to find divisors: "))
divisors(user,user)
