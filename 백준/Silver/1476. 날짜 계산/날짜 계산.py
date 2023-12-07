def years(n):
    return [n]+[i for i in range(1,n)]

E, S, M = map(int,input().split())

for i in range(1,10001):
    e, s, m = years(15)[i%15], years(28)[i%28], years(19)[i%19]
    if E == e and S == s and M == m:
        print(i)
        break