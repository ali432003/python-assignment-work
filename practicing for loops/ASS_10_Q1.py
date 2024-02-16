def fibonacci(user):
    a,b = 0,1
    count = 0
    while count < user:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1

user = int(input("enter range: "))
if user%fibonacci==0:
    print("the number is in fibbonacci series")
else:
    print("the number is not in fibonacci")


def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter range: "))
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i))