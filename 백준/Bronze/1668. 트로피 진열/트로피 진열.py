def cnt_t(arr):
    x, cnt = arr[0], 1
    for i in arr[1:]:
        if i > x:
            cnt += 1
            x = i
    return cnt

arr = [int(input()) for _ in range(int(input()))]
print(cnt_t(arr), cnt_t(arr[::-1]), sep='\n')