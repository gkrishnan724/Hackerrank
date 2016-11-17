s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apples = map(int,raw_input().strip().split(' '))
oranges = map(int,raw_input().strip().split(' '))
cnta = 0
cntb = 0
for i in range(len(apples)):
	fallpnt = apples[i] + a
	if fallpnt <= t and fallpnt >= s:
		cnta += 1

for i in range(len(oranges)):
	fallpnt = oranges[i] + b
	if fallpnt <= t and fallpnt >= s:
		cntb += 1
print cnta
print cntb

	




	