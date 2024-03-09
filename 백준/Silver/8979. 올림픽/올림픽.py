N, K = map(int,input().split())
score = {}
for _ in range(N):
    nation, *medal = input().split()
    score[nation] = int(''.join(medal))
    
print(sorted(score, key= lambda x:score[x] ,reverse=True).index(str(K)))