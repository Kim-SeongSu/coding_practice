'''
# 시간초과
import sys

string = ''
while True:
    try:
        x = sys.stdin.readline().rstrip()
        string += x
    except: 
        break

arr = dict(zip([chr(i) for i in range(97,123)],[string.count(chr(j)) for j in range(97,123)]))

answer = ''    
for k in range(97,123):
    if arr[chr(k)] == max(arr.values()):
        answer += chr(k)
print(answer)
'''
import sys

arr = [0]*26

# sys.stdin.read()를 사용하면 한번에 입력받을 수 있음!
for i in sys.stdin.read().replace('\n','').replace(' ',''):
    arr[ord(i)-97] += 1

print(''.join([chr(idx+97) for idx in range(26) if arr[idx] == max(arr)]))