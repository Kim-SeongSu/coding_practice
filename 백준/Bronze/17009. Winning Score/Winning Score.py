team = [0,0]
score = [3,2,1]
for i in range(2):
  for j in range(3):
    team[i] += int(input())*score[j]
print('A' if team[0]>team[1] else 'T' if team[0]==team[1] else 'B')