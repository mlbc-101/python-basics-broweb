"""Write a program which can compute the factorial of a given numbers."""
fact = 1
while True:
    a = int(input("Enter a number: "))
    if a >= 0:
        break
if a != 0:
    for x in range(1,a+1):
        fact *= x
print(fact)