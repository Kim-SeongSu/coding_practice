a, b = map(int,input().split())
c, n = int(input()), int(input())

print(1 if (c-a)*n >= b and c >= a else 0)