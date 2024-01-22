N = int(input())
arr = [0]*N
h = list(map(int,input().split()))

for i in range(N-1):
    cnt = 0
    for j in range(i+1,N):
        if h[i]>h[j]:
            cnt += 1
        else:
            break
    arr[i] = cnt
print(max(arr))