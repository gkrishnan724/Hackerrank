a,k = raw_input().split(" ")
k = int(k)
c = map(int,raw_input().split(" "))
d = raw_input()
d = int(d)

c.remove(c[k])
s = 0
for i in range(len(c)):
    s = s+c[i]

s = s/2

if s == d:
    print "Bon Appetit"
else:
    print d - s
