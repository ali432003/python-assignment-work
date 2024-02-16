b=int(input("Enter no of boys: "))
g=int(input("Enter no of girls: "))
totalbill=int(input("Enter total cost of bill: "))
totalp=b+g
perhead=totalbill/totalp
onegirl=perhead*0.6
totgirlspay=onegirl*g
oneboy=(totalbill-totgirlspay)/b
totboyspay=oneboy*b
print("share of each:" ,perhead)
print("share of totboys:" ,totboyspay)
print("share of 1 boy:" ,oneboy)
print("share of totgirls:" ,totgirlspay)
print("share of 1 girl:" ,onegirl)


