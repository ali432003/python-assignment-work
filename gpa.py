total_subs = int(input(":"))
subs = []
score = []
# collecting
for i in range(total_subs):
    name = input("Enter name: ")
    s = int(input('score: '))
    subs.append(name)
    score.append(s)

# grading
A = False
B = False
C = False
for i in score:
    if i>=90:
        A = True
    elif i<89 and i<85:
        B = True
    else:
        C= True

# calculating gpa
tot = sum(score)
for i in range(len(score)):
    p = (score[i]/tot)*100  
     
    if p>=90:
        print("A grade")
    elif p<89 and p<85:
        print("B grade")
    else:
        print('fail')     
print('%',p)