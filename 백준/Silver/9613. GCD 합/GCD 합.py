'''
10    1 2     5     10
20    1 2   4 5     10      20
30    1 2 3   5 6   10   15    30
40    1 2   4 5   8 10      20    40

5     1      5
7     1        7
12    1 2 3 4 6 12
'''

from itertools import combinations as cb
from math import gcd

for _ in range(int(input())):
    n, *l = map(int,input().split())
    print(sum([gcd(i,j) for i,j in list(cb(l,2))]))