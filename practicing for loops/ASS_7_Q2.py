#Updating Q1

print("ASSALAMUALAIKUM, THIS IS EVENT DESK KINDLY ENTER YOUR PASS FEE (1200PKR-700PKR) ")

dicount=0
list_dis=[]
total=10 + 30  #10 are participants while other 30 are guests(As the capacitiy of event hall is 100 partcipants) 
desk=0
enter_name=0
name_list=[]
amount_pr_head=[]
total_fees_collected=0

for i in range(total):
    enter_name=input("enter your name : ")
    name_list.append(enter_name)
    fees_paid=int(input("enter fees paid: "))
    while fees_paid<700 or fees_paid>1200:
        fees_paid=int(input("Enter correct Amount: "))
    if desk!=total-1:
        print("\n\t\tthe registration desk is still open")
        desk+=1
    else:
        print("\n\t\t   the registration desk is closed")
    total_fees_collected = total_fees_collected + fees_paid 
    list_dis.append(1200-fees_paid)
    amount_pr_head.append(fees_paid)
    dicount = dicount + (1200-fees_paid)

print("Name\t\tAmount\t\tDiscount")
for i in range(total):
    print(name_list[i],"\t\t",amount_pr_head[i],"\t\t",list_dis[i])
print("total amount collected is : ",total_fees_collected)
print("total discount collected is: ",dicount)

