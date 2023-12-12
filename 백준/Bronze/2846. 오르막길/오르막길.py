N = int(input())
P = list(map(int,input().split()))

x, answer = P[0], [0]
for i in range(1,len(P)):
    if P[i] <= P[i-1]:
        answer.append(P[i-1]-x)
        x = P[i]
answer.append(P[-1]-x)

print(max(answer))