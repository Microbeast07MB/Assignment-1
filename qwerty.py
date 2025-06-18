n=int(input("Enter your number: "))



def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)


print("Factorial of",n, "is: ",factorial(n))


#--------------------------------------------------------------------------------------------------

import math

x=float(input("Enter Number: "))

print("Square Root: ",math.sqrt(x))
print("Logarithm: ",math.log(x))
print("Sine: ",math.sin(x))

