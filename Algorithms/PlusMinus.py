n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos = 0
neg = 0
zero = 0
for i in range(n):
	if arr[i] == 0:
		zero += 1
	elif arr[i] > 0:
		pos += 1
	else:
		neg += 1

print '{0:.6f}'.format(pos/float(n)) #to print in 6 decimal places
print '{0:.6f}'.format(neg/float(n))
print '{0:.6f}'.format(zero/float(n))
		
