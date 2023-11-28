n = int(input())
if n < 100:
    print(n)

else:
    answer = 99
    if n == 1000:
        n = 999
    for i in range(100,n+1):
        x = str(i)
        if int(x[1])-int(x[0]) == int(x[2]) - int(x[1]):
            answer += 1
    print(answer)