import sys

burger = [int(sys.stdin.readline()) for _ in range(3)]
drink = [int(sys.stdin.readline()) for _ in range(2)]

print(min(burger)+min(drink)-50)