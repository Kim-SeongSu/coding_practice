info = []

for i in range(N:=int(input())):
    age,name = map(str,input().split())
    info.append([int(age),i,name])

for i in sorted(info):
    print(i[0],i[-1])