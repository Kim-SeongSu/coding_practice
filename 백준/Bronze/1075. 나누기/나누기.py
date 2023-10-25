import sys

N, F = sys.stdin.readline(), int(sys.stdin.readline())

for i in range(int(N[:-3])%F*100, int(N[:-3])%F*100+100):
    if i % F == 0:
        print('0'+str(i) if i < 10 else str(i)[-2:])
        break