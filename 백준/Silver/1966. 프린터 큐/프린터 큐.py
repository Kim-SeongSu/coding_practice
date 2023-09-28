import sys

for _ in range(int(sys.stdin.readline())):
    n,m = map(int,sys.stdin.readline().split())
    queue = list(map(int,sys.stdin.readline().split()))
    count, arr = 0, [i for i in range(n)]
    arr[m] = 'x'

    while queue:
        if queue[0] == max(queue):
            count += 1
            if arr[0] == 'x':
                print(count)
                break
            queue.pop(0)
            arr.pop(0)
        else:
            queue.append(queue.pop(0))
            arr.append(arr.pop(0))