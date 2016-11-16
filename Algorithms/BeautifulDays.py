i,j,k = map(int,raw_input().split(" "))
cnt = 0
for days in range(i,j+1):
	days = str(days)
	rev = days[::-1]
	if abs(int(rev) - int(days))%k == 0:
		cnt += 1

print cnt