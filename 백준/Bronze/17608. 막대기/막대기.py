arr = [int(input()) for _ in range(int(input()))][::-1]

cnt, x = 0, 0
for i in arr:
    if i > x:
        cnt += 1
        x = i
print(cnt)