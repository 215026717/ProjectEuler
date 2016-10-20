#There exists exactly one Pythagorean triplet for which a + b + c = 1000 = n
#output the product abc
import sys
try:
	n = int(sys.argv[1])
except IndexError:
	n = int(input())
for a in range(1,n):
	b = a
	c = (a ** 2 + b ** 2) ** 0.5
	while (a + b + c) <= n:
		b += 1
		c = (a ** 2 + b ** 2) ** 0.5
		if int(c) == c and (a ** 2 + b ** 2) == c ** 2 and a + b + c == n:
			print(a*b*c)
			break
	else:
		continue
	break
