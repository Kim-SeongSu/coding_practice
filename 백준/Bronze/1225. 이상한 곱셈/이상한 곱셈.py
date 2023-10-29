import sys

A, B = sys.stdin.readline().split()

answer = 0
for i in A:
    for j in B:
        answer += int(i)*int(j)
print(answer)