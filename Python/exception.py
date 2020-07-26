import sys

try:
	x = int(input("x: "))
	y = int(input("y: "))
except ValueError:
	sys.exit("Error: invalid input")

try:
	result = x / y
except ZeroDivisionError:
	sys.exit("Error: cannot divide by 0")

print(f"Result x/y = {result}")
