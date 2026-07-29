import sys
sys.stdin=open('input.txt', 'rt')
import heapq as hq

heap=[]
while True:
  n=int(input())
  if n==-1:
    break
  elif n==0:
    if len(heap)==0:
      print(-1)
    else:
      print(-hq.heappop(heap))
  else:
    hq.heappush(heap, -n)























# arr=[]

# while True:
#   val=int(input())
#   if val==-1:
#     break
#   if val==0:
#     if len(arr)==0:
#       print(-1)
#     else:
#       print(-hq.heappop(arr))
#   else:
#     hq.heappush(arr, -val)

