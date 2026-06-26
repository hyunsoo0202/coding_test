import sys
sys.stdin=open('input.txt', 'rt')
from collections import deque
queue=deque([1,2,3,4,5])

target=input()
n=int(input())

for _ in range(n):
  arr=input()
  queue=deque(target)
  print(queue)
  res='YES'
  cnt=''
  for x in arr:
    if x in queue:
      cnt=queue.popleft()
      if x!=cnt:
        res='NO'
        break
  else:
    if len(queue)!=0:
      res='NO'
  print(res)
  