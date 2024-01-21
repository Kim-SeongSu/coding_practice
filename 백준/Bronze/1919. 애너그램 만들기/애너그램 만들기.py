x, y = input(), input()
print(len(x) + len(y) - 2*(sum([min(x.count(i),y.count(i)) for i in set(x+y)])))