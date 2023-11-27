x = 1000 - int(input())
arr = ['x','500','100','50','10','5','1']

answer = x//500
for i in range(2,7):
    answer += eval('%'.join(arr[:i]))//int(arr[i])
print(answer)