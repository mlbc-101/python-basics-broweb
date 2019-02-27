"""Write a program that solves second degree equation of the form ax^2 +bx + c = 0."""
import math
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
D = (b**2)-(4*a*c)
if (D>0):
    print('X1 = ',(-b-math.sqrt(D))/(2*a))
    print('X2 = ',(-b+math.sqrt(D))/(2*a))
elif (D==0):
    print('X = ',(-b)/(2*a))
else:
    print("No solution")