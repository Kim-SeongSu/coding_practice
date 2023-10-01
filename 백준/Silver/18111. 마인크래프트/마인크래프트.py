# python3는 안됨 pypy3로 변경
import sys

n, m, b= map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

minN, maxN, t, h = min(map(min,arr)), max(map(max,arr)), 99999999, 0

for i in range(minN, maxN+1):
    plus, minus = 0, 0
    for j in range(n):
        for k in range(m):
            if arr[j][k] < i:
                minus += i - arr[j][k]
            else:
                plus += arr[j][k] - i
    
    if plus + b >= minus:
        if 2 * plus + minus <= t:
            t = 2 * plus + minus
            h = i

print(t,h)