import math

def primenumbers(end):
 for num in range(1, end+1):
        if num ==1:
            print("1 is not PrimeNumber")
        elif num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                 if(num % i) == 0:
                        print(num,"is not PrimeNumber ")
                        break
            else:
               print(num,"is PrimeNumber")

end = int(input('Enter the range : '))
primenumbers(end)

   


