def InOut(x,y,cx,cy,r):
    R = (x-cx)**2+(y-cy)**2 -r**2
    return 1 if R>0 else 0

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int,input().split())
    cnt = 0
    for _ in range(int(input())):
        cx, cy, r = map(int,input().split())
        if InOut(x1,y1,cx,cy,r) != InOut(x2,y2,cx,cy,r):
            cnt += 1
    print(cnt)