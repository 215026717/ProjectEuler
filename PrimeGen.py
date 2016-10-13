#generates a list with boolean where if i is prime sieve[i] == True
def prime(n,sieve):
	x = 1
	while x*x < n:
		y = 1
		while y*y < n:
			a = 4*x*x+y*y
			if a <= n and (a % 12 == 1 or a % 12 == 5):
				sieve[a] ^= True
			a = 3*x*x+y*y
			if a <= n and a % 12 == 7:
				sieve[a] ^= True
			a = 3*x*x-y*y
			if x > y and a <= n and a % 12 == 11:
				sieve[a] ^= True
			y+=1
		x+=1
	r = 5
	while r*r < n:
		if sieve[r]:
			for i in range(r*r,n,r*r):
				sieve[i] = False
		r += 1
