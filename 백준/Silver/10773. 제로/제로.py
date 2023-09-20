import sys

answer = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x == 0:
        del answer[-1]
    else:
        answer.append(x)
print(sum(answer) if sum(answer) > 0 else 0)