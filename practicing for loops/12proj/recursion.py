
# n! = 1*2*3*4*5*6....n or
# n! = (n-1)*n
# e.g n = 4 \/\/\/\/\/\/\/\ 4! = (4-1)!*4 = 1*2*3*4 = 24

# through iteration..
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1) #cause initially i = 0 so we incremented it by 1
    return product

print(factorial_iter(4))    

# through recursion..
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)
    
print(factorial_recursive(5))
