#output the largest prime factor of the number n
#isPrime from problem 7
from isPrime import isprime
import sys
def largest(t,l,inter):
	for i in range(l,int(t),inter):
		if t % i == 0:
			return largest((t/i),l,inter)
	return t
try:
	n = int(sys.argv[1])
except IndexError:
	n = int(input())
if n % 2 == 0:
	print(largest(n,2,1))
else:
	print(largest(n,3,2))
