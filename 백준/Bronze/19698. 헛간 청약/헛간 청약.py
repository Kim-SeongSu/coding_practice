N, W, H, L = map(int,input().split())
x = (W//L)*(H//L)
print(x if N > x else N)