def fib(n):
    global cnt_a

    if n == 1 or n == 2:
        cnt_a += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global cnt_b

    f = [0]*(n+1)
    f[1] = f[2] = 1
    
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
        cnt_b += 1
    return f[n]


n = int(input())
cnt_a, cnt_b = 0, 0
fib(n); fibonacci(n)

print(cnt_a, cnt_b)