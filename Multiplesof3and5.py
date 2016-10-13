#the sum of all the multiples of 3 or 5 below n
import sys
def mult(n):
	sum = 0
	for i in range(3,n):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	return sum
try:
	n = int(sys.argv[1])
except IndexError:
	n = int(input)
print("The sum is:",mult(n))
