# 시간초과
import sys

n = int(sys.stdin.readline())
arr = [i**2 for i in range(int(n**0.5)+1)]
result = []

for i in arr:
    for j in arr:
        for k in arr:
            for l in arr:
                if i+j+k+l == n:
                    result.append(4-[i,j,k,l].count(0))

print(min(result))