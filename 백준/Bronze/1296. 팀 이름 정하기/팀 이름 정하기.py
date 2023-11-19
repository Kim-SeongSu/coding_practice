import sys
input = sys.stdin.readline

Yeondu, n = input().strip(), int(input())
team_names, scores = sorted([input().strip() for _ in range(n)]), [0]*n

for i in range(n):
    score, arr = 1, [Yeondu.count(alphabet) + team_names[i].count(alphabet) for alphabet in ['L','O','V','E']]


    for a in range(3):
        for b in range(a+1,4):
            score *= arr[a]+arr[b] 
    scores[i] = score%100
print(team_names[scores.index(max(scores))])
