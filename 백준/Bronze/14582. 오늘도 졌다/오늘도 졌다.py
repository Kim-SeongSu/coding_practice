a = list(map(int,input().split()))
b = list(map(int,input().split()))

score_a, score_b = 0, 0
temp = 0
for i in range(9):
    score_a += a[i]
    
    if score_a > score_b:
        temp = 1
    score_b += b[i]
print('Yes' if temp == 1 else 'No')