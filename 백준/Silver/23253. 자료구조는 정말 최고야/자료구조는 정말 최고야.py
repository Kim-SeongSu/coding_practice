'''
import sys

N, M = map(int,input().split())

arr = [0]*M
for i in range(M):
    k = int(sys.stdin.readline())
    arr[i] = list(map(int,sys.stdin.readline().split()))

book = []
while arr!=[]:
    temp = []
    for i in arr:
        if i == []:
            arr.remove([])
        else:
            temp.append(i.pop())
    if temp != []:
        book.append(min(temp))
        book.append(max(temp))

TF = 1
for i in range(1,len(book)):
    if book[i] < book[i-1]:
        TF = 0
        break
print('Yes' if TF == 1 else 'No')
'''

import sys

N, M = map(int,input().split())
TF = 1

for _ in range(M):
    k = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))
    if arr != sorted(arr,reverse=True):
        TF = 0

print('Yes' if TF == 1 else 'No')