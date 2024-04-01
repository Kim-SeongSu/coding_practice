N, W, H = map(int,input().split())
x = (W**2 +H**2)**0.5

for i in range(N):
    y = int(input())
    print('DA' if x >= y else 'NE')