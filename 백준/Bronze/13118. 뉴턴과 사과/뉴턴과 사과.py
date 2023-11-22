import sys

people = list(map(int,sys.stdin.readline().split()))
x, y, r = map(int,sys.stdin.readline().split())

print(people.index(x)+1 if x in people else 0)
