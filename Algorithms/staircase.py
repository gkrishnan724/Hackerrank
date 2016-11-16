n = int(raw_input().strip())
i = 0
while (i < n):
	w = ""
	s = ""
	r = ""
	j = 0
	spaces = n - (i+1)

	while (spaces > 0):
		s = s +" "
		spaces -= 1
	while (j < i+1):
		w = w + "#"
		j += 1
	r = s+w
	print r
	
	i += 1
	


	
	

