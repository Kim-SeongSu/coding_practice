x = int(input())
bar, cnt = [64,32,16,8,4,2,1], 0

for i in bar:
    if x >= i:
        cnt += 1
        x -= i
    if x == 0:
        print(cnt)
        break