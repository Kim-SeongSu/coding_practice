import sys

arr = dict(zip([chr(i) for i in range(97,123)], [0]*26))

for _ in range(int(sys.stdin.readline())):
    string = sys.stdin.readline()[0]
    arr[string] += 1

answer = ''
for i in arr.keys():
    if arr[i] > 4:
        answer += i
print(answer if answer != '' else 'PREDAJA')