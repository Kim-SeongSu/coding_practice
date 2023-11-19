import sys
input = sys.stdin.readline

N, files, C = int(input()), [i for i in map(int,input().split()) if i > 0], int(input())

print(C*sum([file//C if file%C==0 else file//C+1 for file in files]))