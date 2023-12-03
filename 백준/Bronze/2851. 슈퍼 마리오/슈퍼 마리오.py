import sys

score = 0
for x in [int(sys.stdin.readline()) for _ in range(10)]:
    score += x
    if score > 99:
        if score - 100 > 100 - (score - x):
            score -= x
        break
print(score)