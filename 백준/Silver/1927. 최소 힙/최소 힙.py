'''
#시간초과
arr = []
for _ in range(int(input())):
  x = int(input())
  if x == 0:
    print(min(arr) if arr!=[] else 0)
    if arr != []:
      arr.remove(min(arr))
  else:
    arr.append(x)



import heapq

heap = []
for _ in range(int(input())):
  x = int(input())
  if x == 0:
    print(heapq.heappop(heap) if heap!=[] else 0)
  else:
    heapq.heappush(heap, x)

'''
import sys
import heapq as hq

heap = []
for _ in range(int(sys.stdin.readline())):
  x = int(sys.stdin.readline())
  if x == 0:
    if heap==[]:
      print(0)
    else:
      print(hq.heappop(heap))
  else:
    hq.heappush(heap, x)