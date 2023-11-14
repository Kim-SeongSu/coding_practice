import sys

input = sys.stdin.readline
n = int(input())
score = [[] for _ in range(n)]
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(5):
    for j in range(n):
        for k in range(j+1,n):
            if arr[j][i] == arr[k][i]:
                score[j].append(k+1)
                score[k].append(j+1)
answer = [len(set(x)) for x in score]
print(answer.index(max(answer))+1)