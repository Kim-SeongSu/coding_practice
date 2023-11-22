import sys

X, Y = map(int,sys.stdin.readline().split())
answer = [1000*X/Y]

for _ in range(int(sys.stdin.readline())):
    X, Y = map(int,sys.stdin.readline().split())
    answer.append(1000*X/Y)
print(f'{min(answer):.2f}')