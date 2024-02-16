# Q1
participants = int(input("enter number of participants: "))
total_amount_collected=0
amount_list_of_participants = []
name_list_of_participants = []

for i in range(participants):
    name=input("enter your name:")
    name_list_of_participants.append(name)
    amount  = int(input("enter your amount: "))
    amount_list_of_participants.append(amount)
    total_amount_collected = total_amount_collected + amount

print("NAME\t\tAMOUNT")
for i in range(participants):
  print(name_list_of_participants[i],"\t\t",amount_list_of_participants[i])

print("Total amount collected\n\t" ,total_amount_collected) 
############################################################################################################
#############################################################################################################
#############################################################################################################
# UPDATING Q1
participants = int(input("enter number of participants: "))
total_amount_collected = 0
name_list_of_participants = []
amount_list_of_participants = []
discount_list = []
discount = 0

for i in range(participants):
  name = input("enter your name:")
  name_list_of_participants.append(name)
  amount = int(input("enter your amount: "))
  while amount>1200:
    amount = int(input("PLEASE!! enter your correct amount: "))
  if amount<1200:
    print("your amount is less than 1200, DISCOUNT GIVEN!")
  amount_list_of_participants.append(amount)  
  discount = discount + (1200-amount)
  discount_list.append(1200-amount)
  total_amount_collected = ( total_amount_collected + amount)

print("NAME\t\tAMOUNT\t\tDISCOUNT")
for i in range(participants):
  print(name_list_of_participants[i],"\t\t",amount_list_of_participants[i],"\t\t",discount_list[i])

print("Total amount collected\n\t" ,total_amount_collected) 
print("Total DISCOUNT\n\t" ,discount)



