import sys
result = [0,0]
N, arr = int(sys.stdin.readline()), list(map(int,sys.stdin.readline().split()))

for i in arr:
    result[0] += 10 + i//30*10
    result[1] += 15 + i//60*15

if result[0] == result[1]:
    print('Y', 'M', result[0])
else:
    print(['Y','M'][result.index(min(result))], min(result))