N, cnt = int(input()), 0

while N >= 10:
    N = sum([int(i) for i in str(N)])
    cnt += 1
print(cnt)
print('YES' if N%3==0 else 'NO')