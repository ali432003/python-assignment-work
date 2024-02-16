num1 = int(input("Enter a number between 10 and 20: "))

while num1<=10 or num1>=20:
    if num1<=10:
        print("Too low")
    elif num1>=20:
        print("too high")
    
    num1 = int(input("Enter a number between 10 and 20: "))

print("Thank you") 