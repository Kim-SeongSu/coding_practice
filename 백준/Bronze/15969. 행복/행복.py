import sys

sys.stdin.readline()
score = sorted(map(int,sys.stdin.readline().split()))
print(score[-1]-score[0])