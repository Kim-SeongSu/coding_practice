import sys

input = sys.stdin.readline

n = int(input())
print(sum([1 for i in map(int,input().split()) if n == i]))