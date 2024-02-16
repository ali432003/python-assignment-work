# madlib 

# a_boy_name = input("a boy name:  ")
# any_relation_name = input("any relation name: ") 
# good_feeling = input("good feeling: ") 
# colour = input("favourite colour: ")

# madlib = f"One day {a_boy_name} was running around his house with his {any_relation_name} and \
# then suddenly {a_boy_name} heard his {any_relation_name} slam the door and run away.\
# Then {a_boy_name} screamed and started to cry but then mysteriously his \
# {any_relation_name} appeared out of nowhere in the room! \
# {a_boy_name} was so {good_feeling} that his {any_relation_name} came back he laughed and squealed and \
# it was the best day ever especially when he noticed his clothes had all gone {colour}!"

# print(madlib)

# guess random number(user krega)
# l
# spiecial
import random

def guess(a):
    random_num = random.randint(1,a)
    guess = 0
    while guess != random_num:
        guess = int(input(f"guess a number b/w 1 and {a}: "))
        if guess < random_num:
            print("too low, try again")
        elif guess > random_num:

            print("too high,try again")
    print(f"yay!! u got the num {random_num}")    

a = int(input("enter range of game from 1 to: "))
guess(a)

# guess random number(computer krega)

# def comp_guess(b):
#     low = 1
#     high = b
#     feedback = ""
#     while feedback!='c':
#         if low!=high:
#             guess = random.randint(low,high)
#         else:
#             guess = low    #it may be high coz high = low =guess
#         feedback = input(f"Is {guess} num iss Too high(h) or Too low(l) or correct(c)??  ")
#         if feedback =='h':
#             high = guess-1
#         elif feedback =='l':
#             low = guess + 1
#     print(f"computer guessed correctly num is ,{guess}")               


# b = int(input("enter range of game from 1 to: "))
# comp_guess(b)

# rock paper scisssor (user1 vs user2)


# user1_action = input("Enter a choice (rock, paper, scissors): ")
# user2_action = input("Enter a choice (rock, paper, scissors): ")

# print(f"\nplayer 1 {user1_action}, player 2 {user2_action}.\n")

# if user1_action == user2_action:
#     print(f"Both players selected {user1_action}. It's a tie!")
# elif user1_action == "rock":
#     if user2_action == "scissors":
#         print("Rock smashes scissors! player 1 wins!")
#     else:
#         print("Paper covers rock! player 2 wins!.")
# elif user1_action == "paper":
#     if user2_action == "rock":
#         print("Paper covers rock! player 1 wins!")
#     else:
#         print("Scissors cuts paper! player 2 wins!")
# elif user1_action == "scissors":
#     if user2_action == "paper":
#         print("Scissors cuts paper! player 1 wins!")
#     else:
#         print("Rock smashes scissors! player 2 wins!")

# rock paper scisssor (user vs computer)


# user_action = input("Enter a choice (rock(r), paper(p), scissors(s)): ")
# computer = random.choice(['r','p','s'])

# print(f"\n user choose {user_action}, computer choose {computer}.\n")

# if user_action == computer:
#     print(f"Both selected {user_action}. It's a tie!")
# elif user_action == "r":
#     if computer == "s":
#         print("Rock smashes scissors! user won!!")
#     else:
#         print("Paper covers rock! computer won!!")
# elif user_action == "p":
#     if computer == "r":
#         print("Paper covers rock! user won!!")
#     else:
#         print("Scissors cuts paper! computer won!!" )
# elif user_action == "s":
#     if computer == "p":
#         print("Scissors cuts paper! user won!!")
#     else:
#         print("Rock smashes scissors! computer won!!")

# Hangman
# import string
# import random        
# words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","accept","acceptable","accessible","accidental","account","accurate","achiever","acid","acidic","acoustic","acoustics","acrid","act","action","activity","actor","actually","ad hoc","adamant","adaptable","add","addicted","addition","adhesive","adjoining","adjustment","admire","admit","adorable"]

# def isvalid_word(words):
#     word = random.choice(words)     #koi bhi ek word randomly lelega list mese
#     while '-' in word or ' ' in word:
#         word = random.choice(words) #agr dash wagera aya toh dubara se choice krr
    
#     return word                     #jb bina "-" or " " wla miljayega toh return kra dega


# def hangman():
#     word = isvalid_word(words)
#     word_letters = set(word) #letters in word
#     alphabet = set(string.ascii_uppercase) #capital letter ka set
#     used_letter = set()  #wo letters jo user guess krega
#     lives = 6
#     # getting user input
#     while len(word_letters) > 0 and lives > 0:
#         # letter used
#         # ["a","b","c"]--->"a b cd"
#         print("your lives is",lives,"You have used these letters"," ".join(used_letter)) #"used_letter" is list for converting it into str

#         #curren word i.e(W_R_)
#         word_list = [letter if letter in used_letter else "_" for letter in word] #agr word letter word me hua toh print krdegaa warna "_" dega
#         print("current word: "," ".join(word_list))

#         user_input = input("Enter a letter: ").upper()
#         if user_input in alphabet-used_letter:
#             used_letter.add(user_input)           #agr valid uppercase letter hua toh used me add krdega ye letter
#             if used_letter in word_letters:
#                 used_letter.remove(user_input)    #agr used me pehle se huaa to user ka letter nikal dega
#             else:
#                 lives = lives -1        
#         elif user_input in used_letter:
#             print("you have already guessed that letter , Try again!!") #agr letter pehle se use kiya hua ho then..
#         else:
#             print('wrong letter ,please try again') #ghlt letter input krnee prr  
#     # if word_letter == 0;
#     if lives == 0:
#         print("you died the word is ",word)
#     else:    
#         print("you have guessed the word correctly",word)
              
# hangman()















# # tic ta toe

# import random
# import math

# class player:
#     def __init__(self,letter):
#         # letter is X or O
#         self.letter = letter

        
