import sys

N = int(sys.stdin.readline())

for i in range(N-1,0,-1):
    star = ' '*(N-1-i)+'*'*i
    print(star+'*'+star[::-1].rstrip())
print(' '*(N-1)+'*')
for i in range(1,N):
    star = ' '*(N-1-i)+'*'*i
    print(star+'*'+star[::-1].rstrip())
