N = int(input())

for i in range(1,N+1):
    S = sum(list(map(int,str(i))))

    if i + S == N:
        print(i)
        break

    if i == N:
        print(0)