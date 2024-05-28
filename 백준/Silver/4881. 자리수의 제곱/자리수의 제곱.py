import sys

def isin(n):
    arr, s = [], set()
    while int(n) not in s:
        arr.append(int(n))
        s.add(int(n))
        n = str(sum([int(i)**2 for i in n]))
    return arr, s

while 1:
    N, M = sys.stdin.readline().split()
    if N == M == '0': 
        break

    a, sa = isin(N)
    b, sb = isin(M)

    l = [i for i in sa if i in sb]

    if l == []:
        print(N, M, 0)
    else:
        min_ = 9999999
        for i in l:
            min_ = min(min_,a.index(i)+b.index(i)+2)
        print(N, M, min_)