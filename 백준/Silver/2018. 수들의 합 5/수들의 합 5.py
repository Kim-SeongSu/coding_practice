N, S, cnt = int(input()), [0], 1

for i in range(1,int(N//2)+2):
    S.append(i)
    if sum(S) > N:
        while sum(S) > N:
            del S[0]
    if sum(S) == N:
        cnt += 1
print(cnt if N > 2 else 1)