import sys

answer = ''
for i in range(1, int(sys.stdin.readline())+1):
    answer += f'{i}. {sys.stdin.readline()}'
print(answer)