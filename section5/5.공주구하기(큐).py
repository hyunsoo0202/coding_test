import sys
sys.stdin=open('input.txt', 'rt')
from collections import deque

n,k=map(int, input().split())

arr=[i for i in range(1, n+1)]


dq=deque(arr)
print(dq)

while len(dq)>1:
  cnt=1
  while cnt<3:
    dq.rotate(-1)
    cnt+=1
  dq.popleft()
print(dq)
arr=list(dq)
print(arr[0])























# n,k=map(int, input().split())
# print(n,k)

# arr=list(range(1, n+1))

# queue=deque(arr)
# print(queue)

# while len(queue)>1:
#   for _ in range(k-1):
#     queue.append(queue.popleft())
#   queue.popleft()

# print(queue[0])

