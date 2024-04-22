def loop(n):
    while True:
        if n%2!=0:
            break
        else:
            n//=2
    return n

n = int(input())
if n < 3:
    print(1)
else:
    print(int(loop(n)==1))