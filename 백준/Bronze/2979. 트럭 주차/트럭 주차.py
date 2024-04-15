A, B, C = map(int,input().split())
arr = [0]*100

for _ in range(3):
    s, e = map(int,input().split())
    for i in range(s,e):
        arr[i] += 1

s = 0
for i in arr:
    if i == 1:
        s += A
    elif i == 2:
        s += 2*B
    elif i == 3:
        s += 3*C
print(s)