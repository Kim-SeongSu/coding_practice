'''
# 시간초과
import sys

N, M = map(int,sys.stdin.readline().split())
S = [sys.stdin.readline() for _ in range(N)]
print(sum([1 for _ in range(M) if sys.stdin.readline() in S]))
'''
# 딕셔너리 사용
import sys

N, M = map(int,sys.stdin.readline().split())
S = {sys.stdin.readline():1 for _ in range(N)}
print(sum([1 for _ in range(M) if sys.stdin.readline() in S]))