import sys

answer = 0
for _ in range(5):
    x = int(sys.stdin.readline())
    answer += x if x > 39 else 40
print(answer//5)