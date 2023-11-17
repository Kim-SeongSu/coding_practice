import sys

S = sys.stdin.readline()

answer = []
for i in range(97,123):
    answer.append(str(S.count(chr(i))))
print(' '.join(answer))