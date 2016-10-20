#output the n adjacent digits in the file, num.txt, that have the greatest product.
import sys
try:

	n = int(sys.argv[1])
	#ln = sys.argv[2]
except IndexError:
	n = int(input())
	#ln = input()
ln = open("num.txt","r")
temp = ln.read().splitlines()
nl = (''.join(temp)).split("0")
ret = 0
for v in nl:
	if len(v) >= n:
		for i in range(len(v)):
			mult = 1
			for x in v[i:n+i]:		
				mult *= int(x)
			if mult > ret:
				ret = mult
print(ret)
