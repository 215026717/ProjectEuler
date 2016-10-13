#the sum of the even-valued terms considering the terms in the Fibonacci sequence whose values do not exceed n
import sys
try:
	n = int(sys.argv[1])
except IndexError:
	n = int(input())
sums = [1,2]
even = 0
while sums[-1] < n:
	if sums[-1] % 2 == 0:
		even += sums[-1]
	sums.append(sums[-1]+sums[-2])
print(sums,even)
