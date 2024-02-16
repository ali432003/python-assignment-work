
# def numbersum(m):
#  for i in range(m):
#     m += i
#     print(m)

# u = int(input("Enter range: "))

# numbersum(u)


def numbersum(n):
    if n == 0:
        return n
    else:
        return n + numbersum(n-1)

u = int(input("Enter range: "))

print("the total sum is: ",numbersum(u))
