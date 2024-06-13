import sys

for _ in range(int(input())):
    N = int(sys.stdin.readline()) 
    arr = set(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline()) 
    for i in list(map(int,sys.stdin.readline().split())):
        print(int(i in arr))