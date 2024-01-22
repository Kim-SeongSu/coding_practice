s = input()
print(min(len(s.replace('0',' ').replace('1','x').strip().split()), len(s.replace('0','x').replace('1',' ').strip().split())))