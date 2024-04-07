N = int(input())
player = [0]*N
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(3):
    l = [p[i] for p in arr]
    x = set([num for num in l if l.count(num) < 2])

    for n in range(N):
        if arr[n][i] in x:
            player[n] += arr[n][i]
print(*player, sep='\n')