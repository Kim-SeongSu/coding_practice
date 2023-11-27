n = int(input())

if n == 0:
    print(0)
else:
    bp = [0]*(n+1)
    bp[0], bp[1] = 0, 1

    for i in range(2,n+1):
        bp[i] = bp[i-1] + bp[i-2]

    print(bp[n])