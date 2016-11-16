n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
res = 0
for i in range(len(arr)):
    res = res+arr[i]
print res