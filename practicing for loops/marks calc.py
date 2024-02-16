total =0
Name = input("enter your Name :")
b3=Name.upper()
o =input("enter your Grade :")
total_marks=int(input("enter total marks"))
marks=int(input("enter marks obtained: "))

for i in range():
    e=int(input("enter marks in english: "))
    m=int(input("enter marks in maths "))
    u=int(input("enter marks in urdu: "))
    i=int(input("enter marks in islamiat: "))
total=e+m+u+i

p=(total/total_marks)*100
print(p)
if p<50:
   a= print("Grade : F")
elif p>=50  and p<60:
    a=print("Grade : C")
elif p>=60  and p<70:
    a=print("Grade : B")
elif p>=70 and p<80:
    print("Grade : A")
elif p>=80:
    a=print("Grade : A+")
    print (a)
print( b3,"\n","CLASS :",o,"\n","percentage=",p)