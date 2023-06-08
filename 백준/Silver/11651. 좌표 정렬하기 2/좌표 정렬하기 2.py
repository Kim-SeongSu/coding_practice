result = []

for _ in range(int(input())):
    x,y = map(int,input().split())
    result.append([y,x])

for i in sorted(result):
    print(i[1], i[0])