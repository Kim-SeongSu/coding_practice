import sys
input = sys.stdin.readline

N = int(input())
minutes = list(map(int,input().split()))
minutes.sort()
minimum = 0

for index in range(N):
    for i in range(index+1):
        minimum += minutes[i]

print(minimum)