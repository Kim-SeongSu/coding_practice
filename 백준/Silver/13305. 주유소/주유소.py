N = int(input())
dist = list(map(int,input().split()))[::-1]
cost = list(map(int,input().split()))[::-1][1:]

print(sum([min(cost[i:])*dist[i] for i in range(N-1)]))