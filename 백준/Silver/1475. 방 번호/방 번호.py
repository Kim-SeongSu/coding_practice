N = input()
print(max([N.count(str(i)) for i in [0,1,2,3,4,5,7,8]] + [(N.count('6')+N.count('9')+1)//2]))