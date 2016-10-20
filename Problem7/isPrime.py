def isprime(n):
	t = n / 3
	if t == int(t):
		return False
	elif n < 25:
		return True
	elif int(t) % 2 == 0:
		for i in range(int(t)-1,3,-2):
			if n % i == 0:
				return False
		return True
	else:
		for i in range(int(t),3,-2):
			if n % i == 0:
				return False
		return True
