'''
# 41점 (시간 초과)
N = int(input())
dist = list(map(int,input().split()))[::-1]
cost = list(map(int,input().split()))[::-1][1:]
print(sum([min(cost[i:])*dist[i] for i in range(N-1)]))
'''

N = int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))[:-1]
min_c, t = 9999999999, 0
for i in range(N-1):
    if cost[i]<min_c:
        min_c = cost[i]
    t += dist[i]*min_c
print(t)