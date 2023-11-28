N, B = map(int,input().split())

arr = dict(zip([i for i in range(B)],[str(j) for j in range(10)]+[chr(k+55) for k in range(10,B)]))
answer = ''

while N > 0:
    answer += arr[N%B]
    N //= B
print(answer[::-1])