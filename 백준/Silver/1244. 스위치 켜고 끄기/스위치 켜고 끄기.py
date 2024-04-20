N = int(input())
arr = list(map(int,input().split()))

for _ in range(int(input())):
    s, x = map(int,input().split())
    if s == 1:
        for i in range(x-1,N,x):
            arr[i] = int(not arr[i])
    else:
        back = arr[:x-1][::-1]
        front = arr[x:]

        l,k = min(len(back),len(front)), 0

        for i in range(l):
            if back[i] != front[i]:
                k = i
                break
            k += 1

        for i in range(x-1-k,x+k):
            arr[i] = int(not arr[i])

if N < 21:
    print(*arr)
else:
    for i in range(0,N,20):
        print(*arr[i:i+20]) 