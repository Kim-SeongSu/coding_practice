n, arr, score = int(input()), input(), [0,0]

for i in range(n):
    if arr[i] == 'A': score[0] += 1
    else: score[1] += 1
print('Tie' if score[0] == score[1] else ['A','B'][score.index(max(score))])