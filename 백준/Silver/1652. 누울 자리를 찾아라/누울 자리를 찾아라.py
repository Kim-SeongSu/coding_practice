N = int(input())
arr = [input() for _ in range(N)]
arr_r = [''.join([arr[j][i] for j in range(N)]) for i in range(N)]

x, y = 0, 0
for i in range(N):
    x += sum([1 for j in [eval(j) for j in arr[i].replace('.','+1').replace('X',' ').split()] if j > 1])
    y += sum([1 for j in [eval(j) for j in arr_r[i].replace('.','+1').replace('X',' ').split()] if j > 1])
print(x, y)