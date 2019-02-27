"""
Write a program which will find and display all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
"""
for x in range(2000, 3200):
	if (x % 7 == 0) and not(x % 5 == 0):
		print(x)