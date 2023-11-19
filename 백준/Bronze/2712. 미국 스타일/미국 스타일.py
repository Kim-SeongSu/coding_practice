import sys

input = sys.stdin.readline

unit_name = ['kg', 'lb', 'kg', 'l', 'g', 'l']
unit_number = [2.2046, 0.4536 ,2.2046, 0.2642, 3.7854, 0.2642]
for _ in range(int(input())):
    n, weight = input().split()
    x = unit_name.index(weight)+1
    print(f'{float(n)*unit_number[x-1]:.4f} {unit_name[x]}')