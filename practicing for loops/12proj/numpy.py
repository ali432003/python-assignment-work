# Assignment

# Ques 1
import numpy as np

x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])

same = []
notsame = []
for i in range(len(x))or(len(y)):
    if x[i]==y[i]:
        same.append(i)
    else:
        notsame.append(i)

print(f"(array{notsame},) and (array{same}),)")      

# Ques 2

x = np.random.randint(30,40,10) # syntax = (min,max,total_values)
print(x)

# Ques 3

exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

new = []

for items in exercise_1:
    if items%2!=0:
        items = -1
        new.append(items)
    else:
        new.append(items)


print(new)        