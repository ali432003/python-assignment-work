
amount_due = 50

while amount_due>0:
    print("amount due: $",amount_due)
    a = int(input("insert coin: "))
    if a in [5,10,25]:  # bcz coins are of $5 , $10 , $25..
        amount_due = amount_due - a

change = abs(amount_due)
print("changed owned",change)



 
