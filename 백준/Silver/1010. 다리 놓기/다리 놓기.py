'''
# 시간 초과
from itertools import combinations as cb

for _ in range(int(input())):
    N, M = map(int,input().split())
    print(len(list(cb(list(range(M)),N))))

'''
from math import factorial as ft

for _ in range(int(input())):
    N, M = map(int,input().split())
    # mCn = m! / (m-n)!n!
    print(ft(M) // ft(N) // ft(M-N))