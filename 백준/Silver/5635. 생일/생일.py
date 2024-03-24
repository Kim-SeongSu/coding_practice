arr = []
for _ in range(int(input())):
    name, *birth = input().split()
    arr.append([name] + list(map(int,birth)))

arr.sort(key = lambda x : (x[3], x[2], x[1]))

print(arr[-1][0], arr[0][0], sep='\n')