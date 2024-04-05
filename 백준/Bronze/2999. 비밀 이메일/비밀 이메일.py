ipt = input()
N = len(ipt)

R = max([i for i in range(1,N//2+1) if N%i == 0 and i <= N//i])
C = N//R

arr, cnt = [['']*R for _ in range(C)], 0
for i in range(C):
    for j in range(R):
        arr[i][j] = ipt[cnt]
        cnt += 1

result = ''
for j in range(R):
    for i in range(C):
        result += arr[i][j]
print(result)