#the sum of all the primes below n
from PrimeGen import prime
import sys
try:
	n = int(sys.argv[1])
except IndexError:
	n = int(input())
sieve = [False] * n
prime(n,sieve)
sum = 0
for i in range(n):
	if sieve[i]:
		sum += i
print(2+3+sum)
