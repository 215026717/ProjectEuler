#Program that finds prime number i < n that has the longest consecutive primes sum for a given limit n
#i.e. p(1)+p(2)+...+p(l) = i < n
from PrimeGen import prime
import sys,copy
try:
    n = int(sys.argv[1])
except IndexError:
    n = int(input())
pn = [2]
cons = [[2]]
sieve = [False] * n
prime(n,sieve)
sieve[3] = True
for a in range(3,n,2):
	if sieve[a]:
		pn.append(a)
		sub = 0
		rec = cons.index([pn[-2]])
		for ind in range(len(cons[rec:])):
			if rec-ind-1 >= 0:
				if (sum(cons[rec-ind-1]) >= n):
					del cons[rec-ind-1]
					sub += 1
				elif not sieve[sum(cons[rec-ind-1])]:				
					del cons[rec-ind-1]
					sub += 1
			if (sum(cons[rec+ind-sub])+pn[-2]) > n:
				del cons[rec+ind-sub:]
				break
			cons[rec+ind-sub].append(a)
		cons.append([a])
		cons.extend(copy.deepcopy(cons[rec-sub:-1]))
cons.sort(key = len)

for v in cons[::-1]:
    if sum(v) in pn:
        print("it's",sum(v))
        break
