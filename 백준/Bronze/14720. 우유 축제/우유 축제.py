N = int(input())
cnt, x = 0, 0
for i in map(int,input().split()):
    if i == x:
        cnt += 1
        if x < 2:
            x += 1
        else:
            x = 0
print(cnt)