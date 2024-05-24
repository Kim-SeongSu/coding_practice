'''
# 시간초과
while 1:
    N, M = map(int,input().split())
    if N == M == 0:
        break
    arr = [int(input()) for  _ in range(N)]
    
    print(sum([1 for _ in range(M) if int(input()) in arr]))
'''
import sys

while 1:
    N, M = map(int,sys.stdin.readline().split())
    if N == M == 0: break;
        
    arr = set([int(sys.stdin.readline()) for  _ in range(N)])
    print(sum([1 for _ in range(M) if int(input()) in arr]))