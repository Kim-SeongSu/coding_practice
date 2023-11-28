N, arr = int(input()), map(int,input().split())
B, C = map(int,input().split())

answer = 0
for A in arr:
    x = A-B if A>B else 0
    if x%C == 0:
        answer += 1 + x//C
    else:
        answer += 2 + x//C
print(answer)