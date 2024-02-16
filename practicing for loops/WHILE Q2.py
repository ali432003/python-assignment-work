from tkinter.messagebox import YES


total = 0
while True:
    lumber1 = int(input('enter 1st number: '))
    lumber2 = int(input("enter 2nd number: "))
    total = lumber1 + lumber2
    print("\nthe sum of 2 numbers is: " ,total)
    a = input('do you want to add another number (Yes or No): ').lower()
    if a=="yes":
        continue
    elif a=="no":
       print("thanks! the total is: " ,total)
       break
    else:
        print("ERROR!! TRY AGAIN")
        a = input('do you want to add another number (Yes or No): ')
    