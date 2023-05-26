N = int(input())

'''
시간을 단축시키기 위해 아래와 같이 반복문 range 시작값을 정해줬는데 오류가 발생함.

이유는 아직 모름
G = N - int('999999'[:len(str(N))-1]) if N > 10 else N

for i in range(G,N+1):
'''

for i in range(1,N+1):
    S = sum(list(map(int,str(i))))

    if i + S == N:
        print(i)
        break

    if i == N:
        print(0)
