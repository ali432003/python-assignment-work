# def fibonacci(n):
#     if(n <= 1):
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
# user = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(user):
#     print(fibonacci(i))

# def squaring(user):
#     a = 0
#     for i in range(0,user):
#         a += user
#     print(a)

# user = int(input("enter a num: "))
# print("square is ")
# squaring(user)         

    
# def sum_of_even(n):
#     if n == 0:
#         return n
#     else:
#         return n + sum_of_even(n-1)

# u = int(input("Enter range: "))

# print("the total sum is: ",sum_of_even(u))

# def divisors(integer):
#     for i in range(1, integer+1):
#         if divisors(integer) % i == 0:
#             print(i)


# integer = int(input("Please enter any integer to find divisors: "))

# print("divisors are: ")
# divisors(integer)

# def factors(x,i):
#     if i==0:
#         return 
#     if x%i == 0:
#         print(i)
#     return factors (x,i-1) 

# user = int(input("Please enter any integer to find divisors: "))
# factors(user,user)


# for i in range(7):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print("\n")    

# for k in range(8):
#     for z in range(k+1):
#         print("* ",end="") 
#     print("\n")

def prime(n):
    for n in range(1,n+1):
        if n==1:
            print("1 is not prime")
        if n > 1:
            for i in range(2,n):
                if n%i == 0:
                    print(n,"not prime")
                    break
            else:
                print(n,"prime")

n = int(input())
prime(n)                   

# def even_odd(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")


# even_odd(10)


# dic1_1 = {i:f"item{i}" for i in range(50,100) if i%2==0}

# print(dic1_1)














