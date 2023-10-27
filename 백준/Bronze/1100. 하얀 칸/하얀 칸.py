import sys

answer = 0
for i in range(8):
    arr = sys.stdin.readline().rstrip()
    if i % 2 == 0:
        answer += sum([1 if arr[x] == 'F' else 0 for x in range(0,8,2)])
    else:
        answer += sum([1 if arr[x] == 'F' else 0 for x in range(1,8,2)])
print(answer)