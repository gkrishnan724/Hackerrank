n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
cnt = 0


for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i]+a[j])%k == 0:
            cnt += 1



print cnt
