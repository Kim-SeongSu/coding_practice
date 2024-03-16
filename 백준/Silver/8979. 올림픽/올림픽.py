N, K = map(int,input().split())
score = [list(map(int,input().split())) for _ in range(N)]
score.sort(key= lambda x:(-x[1], -x[2], -x[3]))

for i in range(N):
    if score[i][0] == K:
        index = i
for i in range(N):
    if score[index][1:] == score[i][1:]:
        print(i + 1)
        break