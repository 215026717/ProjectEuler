def pal(n):
	sn = str(n)
	if len(sn) % 2 == 0:
		if sn[:int(len(sn)/2)] == sn[int(len(sn)/2):][::-1]:
			return True
		return False
	else:
		if sn[:int(len(sn)/2)] == sn[int(len(sn)/2+1):][::-1]:
			return True
		return False
