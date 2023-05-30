import sys

input = sys.stdin.readline

N_list = [0] * 10000

for i in range(N:= int(input())):
    N_list[int(input())-1] += 1

for i in range(10000):
    if N_list[i] != 0:
        for _ in range(N_list[i]):
            print(i+1)