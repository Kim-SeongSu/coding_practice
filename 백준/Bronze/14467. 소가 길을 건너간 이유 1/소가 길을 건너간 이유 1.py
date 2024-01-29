cow, cnt = dict(zip([str(i) for i in range(11)],[2]*11)), 0

for _ in range(int(input())):
    n, p = input().split()
    if cow[n] == 2:
        cow[n] = int(p)
    else:
        if cow[n] != int(p):
            cnt += 1
            cow[n] = int(p)
print(cnt)