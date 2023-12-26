arr = [False,False]+[True]*1000000
for i in range(2,1000001):
    if arr[i]:
        for j in range(2*i,1000001,i):
            arr[j] = False


for _ in range(int(input())):
    N = int(input())
    OX = True
    for i in range(2,min(1000001,int(N**0.5)+1)):
        if arr[i] and not N%i:
            OX = False
            break
    print('YES' if OX else 'NO')