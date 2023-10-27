import sys

colors = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
arr = [colors[sys.stdin.readline().rstrip()] for i in range(3)]
print((arr[0]*10+arr[1])*(10**arr[2]))