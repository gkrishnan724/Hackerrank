n,k,q = map(int,raw_input().split(" "))
query = []
a = raw_input().split(" ")
for j in range(k):
	temp = a[len(a) - 1]
	for i in range(n-1,0,-1):
		a[i] = a[i-1]
		
	a[0] = temp
	

for i in range(q):
	r = raw_input()
	query.append(int(r))

for i in range(len(query)):
	print a[query[i]]



