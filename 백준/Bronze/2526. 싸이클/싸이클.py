N, P = map(int,input().split())
arr = [N]

x = N
while 1:
    x = x*N%P
    
    if x in arr:
        break
    else:
        arr.append(x)

print(len(arr)-arr.index(x))