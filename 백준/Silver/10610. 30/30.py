''' 10610번
# 시간초과
arr = sorted(input(),reverse=True)
N = int(''.join(arr))

if N < 30:
    print(-1)
else:
    x = 0
    for i in range(30*(N//30),29,-30):
        if sorted(str(i),reverse=True) == arr:
            print(i)
            x = 1
            break
    if x == 0: print(-1)
'''
# 3의 배수는 모든 자리수의 합이 3의 배수
arr = sorted(input(),reverse=True)

if '0' not in arr: 
    print(-1)
else:
    S = sum([int(i) for i in arr])
    print(''.join(arr) if S%3 == 0 else -1)