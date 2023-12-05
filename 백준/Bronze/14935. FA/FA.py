x = input()
arr = [0]*100

for i in range(1,100):
    x = int(str(x)[0])*len(str(x))
    arr[i] = x
print('FA' if arr[-1] == arr[-2] else 'NFA')
