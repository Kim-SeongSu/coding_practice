import sys

input = sys.stdin.readline

arr = {1:'A', 2:'B', 3:'C', 4:'D', 0:'E'}
for _ in range(3):
    x = input().count('0')
    print(arr[x])