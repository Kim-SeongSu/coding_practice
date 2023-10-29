import sys

N = int(sys.stdin.readline())

for i in range(1,N):
    star = '*'*i+' '*(N-i)
    print(star+star[::-1])
print('*'*(2*N))
for i in range(N-1,0,-1):
    star = '*'*i+' '*(N-i)
    print(star+star[::-1])