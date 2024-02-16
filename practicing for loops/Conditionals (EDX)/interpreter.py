exp = input('Expression: ')

x,y,z = exp.split(" ")
# where x & z are integers while y is function like + , - ,* , /
# print(type(x))
# print(type(z))

# as .split only splits string so first we make them int.. 
x = int(x)
z = int(z)

# print(type(x))
# print(type(z))
    
if y=='+':
    print(f'Sum of {x} and {z} is: ',float(x+z))
elif y=='-':
    print(f'Difference of {x} and {z} is: ',float(x-z))
elif y=='*':
    print(f'Product of {x} and {z} is: ',float(x*z))
elif y=='/':
    if z==0:
        print('Maths Error')
    else:
        print(f'Ratio of {x} and {z} is: ',float(x/z))    
elif y=="^":
    print(f'{x} raise to the power {z} is: ',float(x**z))    
elif y=="sqrt":
    import math
    z = 1
    print(f'{x} sqrt is: ',math.sqrt(x*z))    



    

