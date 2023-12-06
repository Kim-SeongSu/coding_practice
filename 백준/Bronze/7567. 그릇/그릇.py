d = input()
print(sum([5 if d[i-1] == d[i] else 10 for i in range(1,len(d))])+10)