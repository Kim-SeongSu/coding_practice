def is_primes(n):
    arr, primes = [False]*2 + [True]*(n-1), []

    for i in range(2,n+1):
        if arr[i] == True:
            primes.append(i)
            for j in range(2*i, n+1, i):
                arr[j] = False

    return primes

a,b = map(int,open(0).readline().split())

for i in is_primes(b):
    if i >= a:
        print(i)