import sys

score = [int(sys.stdin.readline()) for i in range(6)]
print(sum(sorted(score[:4])[1:],max(score[4:])))