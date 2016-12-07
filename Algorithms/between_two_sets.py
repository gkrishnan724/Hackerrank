n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
s1 = map(int,raw_input().strip().split(' '))
s2 = map(int,raw_input().strip().split(' '))
lim = max(max(s1),max(s2))
cnt = 0
if 1 in s1:
    i = 1
else:
    i = 2
while(i <= lim):
    if(all(x%i == 0 for x in s2) and all(i%x == 0 for x in s1)):
        cnt += 1
        
    i += 1

print cnt
