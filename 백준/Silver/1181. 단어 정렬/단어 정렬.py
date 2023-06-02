import sys
input = sys.stdin.readline

N = int(input())

Words = ['']*N

for i in range(N):
    Words[i] = input().rstrip()

for i in range(len(min(temp:=sorted(list(set(Words))), key=len)), len(max(temp, key=len))+1):
    for j in temp:
        if i == len(j):
            print(j)