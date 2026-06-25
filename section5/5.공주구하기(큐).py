import sys
sys.stdin=open('input.txt', 'rt')
from collections import deque

n,k=map(int, input().split())
print(n,k)

arr=list(range(1, n+1))

queue=deque(arr)
print(queue)

while len(queue)>1:
  for _ in range(k-1):
    queue.append(queue.popleft())
  queue.popleft()

print(queue[0])

