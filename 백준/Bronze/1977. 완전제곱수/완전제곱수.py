M, N = int(input()), int(input())
x, y = int(M**0.5), int(N**0.5)

if x**2 < M:
    x += 1

arr = [i**2 for i in range(x,y+1)]

print(f'{sum(arr)}\n{arr[0]}' if arr != [] else -1)