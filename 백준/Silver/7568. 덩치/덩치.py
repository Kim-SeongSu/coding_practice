import sys
input = sys.stdin.readline

xy_list = []

for _ in range(N:= int(input())):
    x,y = map(int,input().split())
    xy_list.append([x,y])

for i in xy_list:
    rank = 1
    for j in xy_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')