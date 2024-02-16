from ast import If


user = input("I LOVE YOU...Waiting for your reply PLZ ans in y/n: ")

if user == "y":
    date = input("wanna go out for a date? press 'y' for yess and 'l'for later: ")
    if date =="y":
       bill = input('''Ok! i'll catch u up at night? but you pay the bill :) press 'f' for getlost and 'o' for Ok: ''')
    if  bill == 'f':
               print("SAME TO U COLD-HEARTED WAHMEN")
    if bill =="o":
               print("me nhi leejaonga :D")
    if date =="l":
       a = input("KB ayi gi wo kl? ")
       if a =='kbhi nhi':
         print("OK i'll go for next candidate")     
    
else: 
 input("REASON :( : ")
 print("fine i'll go for next candidate!!")



