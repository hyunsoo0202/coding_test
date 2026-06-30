import heapq as hq
import sys
sys.stdin=open('input.txt', 'rt')

arr=[]

while True:
  val=int(input())
  if val==-1:
    break
  elif val==0:
    if len(arr)==0:
      print(-1)
    else:
      print(hq.heappop(arr))
  else:  
    hq.heappush(arr, val)
  