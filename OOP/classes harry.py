''' Class Intro and Objects: The class describes what the object will be, 
but is separate from the object itself. 
In other words, a class can be described as an object's blueprint, 
description, or definition.'''

# class Triangle():
#     def __init__(self,length,breath,base):
#         self.length = length
#         self.breath = breath
#         self.base   = base
#     def area(self):
#         return (self.length*self.base)/2
#     def perimeter(self):
#         return self.length+self.breath+self.base
#     def display(self):
#         print('length: ',self.length)
#         print('breath: ',self.breath)
#         print('base: ',self.base)
#         print('area: ',self.area())
#         print('perimeter: ',self.perimeter())
        

# l = int(input('enter length: '))
# br = int(input('enter breath: '))
# ba = int(input('enter base: '))

# ob_tri = Triangle(l,br,ba)
# ob_tri.display()

# class Rectangle():
#     def __init__(self , width , height):
#         self.width = width
#         self.height = height 
#     def area(self):
#         return self.width * self.height #(area = a * b )
#     def perimeter(self):
#         return 2*(self.width + self.height)           #P = 2(l+w)
#     def display(self):
#         print('width: ',self.width)  
#         print('height: ',self.height)
#         print('area: ',self.area())
#         print('perimeter: ',self.perimeter())



# l = int(input("enter height: "))
# w = int(input("enter width: "))

# ob_1 = Rectangle(l,w)
# ob_1.display()

'''Class inheritance and variable'''

# class Employee():
#     increment = 1.6  # class variable 
#     no_of_employe = 0  # class variable 
#     def __init__(self,fname,lname,salary):
#         self.fname = fname # instance variable
#         self.lname = lname
#         self.salary= salary
#         Employee.no_of_employe += 1 # incremneted 1 in class variable
#     def increase(self):
#         self.salary = int(self.salary * self.increment)

# print(Employee.no_of_employe)
# Ali = Employee('Ali','Amir',4500)
# Bilal = Employee('Bilal','Ahmed',4500)
# print(Employee.no_of_employe)
# print()
# print(Ali.salary) # first it searches inside init 
# Ali.increase()
# print(Ali.salary) # but if you direct called the class it goes on class variable


# class Cat():
#     def __init__(self,name,colour,breed):
#         self.name = name
#         self.breed = breed
#         self.colour = colour 
   
# cat_ob = Cat('billo','black','persian')
# print(cat_ob.__dict__) # can return all init variables in dictionary
# cat_ob.legs = 4        # also add variables in init
# print(cat_ob.__dict__)
# print(cat_ob.breed)

''' Class Methods'''

class Employee():
    increment = 1.6  # class variable 
    no_of_employe = 0  # class variable 
    def __init__(self,fname,lname,salary):
        self.fname = fname # instance variable
        self.lname = lname
        self.salary= salary
        Employee.no_of_employe += 1 # incremneted 1 in class variable
    def increase(self):
        self.salary = int(self.salary * self.increment)
    
    @classmethod  # decorator
    def change_increase(cls,amount): # it directly take whole class as arrgument
        cls.increment *= cls.increase() 


print(Employee.no_of_employe)
Ali = Employee('Ali','Amir',4500)
Bilal = Employee('Bilal','Ahmed',4500)
print(Employee.no_of_employe)
print()
print(Ali.salary) # first it searches inside init
print() 
Employee.increase()
Employee.change_increase(2)

print(Ali.salary)        