import sys
import heapq as hq

heap = []
for _ in range(int(sys.stdin.readline())):
  x = int(sys.stdin.readline())
  if x == 0:
    if heap==[]:
      print(0)
    else:
      print(hq.heappop(heap)[1])
  else:
    hq.heappush(heap, (-x,x))