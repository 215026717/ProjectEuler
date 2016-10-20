#output the n-st prime number
from isPrime import isprime
import sys
try:
	n = int(sys.argv[1])
except IndexError:
	n = int(input())
p = 3
num = 5
while p != n:
	num += 2
	if isprime(num):
		p += 1
print(num)
