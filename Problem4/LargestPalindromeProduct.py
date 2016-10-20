#output the largest palindrome made from the product of two n-digit numbers
from Palindrome import pal
import sys
try:
	n = int(sys.argv[1])
except IndexError:
	n = int(input())
lim = (10**(n))
low = (10**(n-1))-1
num = 0
for i in range(lim-1,(10**(n-1))-1,-1):
	for j in range(i,(10**(n-1))-1,-1):
		if pal(i*j) and num < i*j:
			num = i*j
			i1 = i
			j1 = j
			break
print(i1,"x",j1,"=",num)
