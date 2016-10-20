#output the smallest positive number that is evenly divisible by all of the numbers from 1 to n
import sys
try:
	n = int(sys.argv[1])
except IndexError:
	n = int(input())
"""sys.setrecursionlimit(n*5000)
def mult(mini,mul):
	if mini == mul:
		return mul
	for x in d:
		if mini % x != 0:
			return mult(mini+d[-1],mul)
	return mini"""
d = list(range(2,n+1))
mul = 1
for v in d:
	mul *= v
t = 0
mini = d[-1]*d[-2]
while t == 0 and mini != mul:
	for x in d:
		if mini % x != 0:
			t = 0
			mini += d[-1]
			break
		t = 1
print(mini)
