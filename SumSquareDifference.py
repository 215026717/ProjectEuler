#output the difference between the sum of the squares of the first n natural numbers and the square of the sum
from SumNatural import sumN
from SquareNatural import square
import sys
try:
	n = int(sys.argv[1])
except IndexError:
	n = int(input())
a = sumN(n)
b = square(n)
print(a,"-",b,"=",a-b)
