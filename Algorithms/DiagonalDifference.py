n = int(raw_input().strip())
Matrix = [map(eval, raw_input().split(" ")) for i in range(n)]
diag1 = 0
diag2 = 0
for i in range(n):
	for j in range(n):
		if i == j:
			diag1 += Matrix[i][j]
		if i + j == n-1:
			diag2 += Matrix[i][j]


res = diag1 - diag2
print abs(res)