N = int(input())

x = 1
while N>len(str(x)):
    N -= len(str(x))
    x += 1
print(str(x)[N-1])