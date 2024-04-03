N, d = int(input()), int(input())

if N == 1:
    print(0)
else:
    etc = sorted([int(input()) for _ in range(N-1)])
    cnt = 0

    while d <= max(etc):
        d += 1
        etc[-1] -= 1 
        etc = sorted(etc)
        cnt += 1
    print(cnt)