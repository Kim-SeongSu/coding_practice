import sys

def cal(a,b):
    for i in range(1,arr['L']+1):
        if i*b >= a:
            return i

arr_1, arr_2 = ['L','A','B','C','D'], [0]*5

for i in range(5):
    arr_2[i]= int(sys.stdin.readline().rstrip())

arr = dict(zip(arr_1,arr_2))

print(arr['L'] - max(cal(arr['A'],arr['C']),cal(arr['B'],arr['D'])))