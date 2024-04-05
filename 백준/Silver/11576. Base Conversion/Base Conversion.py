A, B = map(int,input().split())
m, x = int(input())-1, 0
for i in list(map(int,input().split())):
    x += i*(A**m)
    m -= 1

answer = []
while x >= B:
    answer.append(str(x%B))
    x //= B
answer.append(str(x))
print(' '.join(answer[::-1]))