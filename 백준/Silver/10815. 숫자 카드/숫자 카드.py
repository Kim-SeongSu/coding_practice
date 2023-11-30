import sys

N = int(input())
N_card = list(sys.stdin.readline().split())

M = int(input())
M_card = dict(zip(list(sys.stdin.readline().split()), [0]*M))

for i in N_card:
    if i in M_card:
        M_card[i] += 1
print(*M_card.values())