# ASSIGNMENT : 07
# Q1

print("ASSALAMUALAIKUM, THIS IS EVENT DESK KINDLY ENTER YOUR PASS FEE (2000PKR) ")

total=3  #10 are participants while other 30 are guests(As the capacitiy of event hall is 100 partcipants) 
desk=0
enter_name=0
name_list=[]
amount_pr_head=[]
total_fees_collected=0
pass_fees = 0

for i in range(total):
    enter_name=input("enter your name : ")
    name_list.append(enter_name)
    fees_paid=int(input("enter fees paid: "))
    while fees_paid!=2000:
        fees_paid = int(input("jfhqejhf:"))    
    if desk!=total-1:
        print("\n\t\tthe registration desk is still open")
        desk+=1
    else:
        print("\n\t\t   the registration desk is closed")
    total_fees_collected = (total*2000)
    amount_pr_head.append(fees_paid)

print("Name\t\tAmount")
for i in range(total):
    print(name_list[i],"\t\t",amount_pr_head[i])
print("total amount collected is : ",total_fees_collected)



