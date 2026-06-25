import sys
sys.stdin=open('input.txt', 'rt')

from collections import deque

n,m=map(int, input().split())
arr=[(x, idx) for idx, x in enumerate(list(map(int, input().split())))]
# print(arr)
queue=deque(arr)
# print(queue)

cnt=0


while True:
  # print(queue)
  x=queue.popleft()  

  if any(x[0]<i[0] for i in queue):
    queue.append(x)
  else:
    cnt+=1
    if x[1]==m:
      break

  # for y in queue:
    
  #   if x[0]<y[0]:
  #     queue.append(x)
  #     break
  # else:
  #   cnt+=1
  #   if x[1]==m:
  #     break
      
print(cnt)



