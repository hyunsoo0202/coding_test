import sys
sys.stdin=open('input.txt', 'rt')
from collections import deque

n=int(input())
options=dict()
for i in range(n):
  options[input()]=1

for i in range(n-1):
  options[input()]=0

for key, val in options.items():
  if val==1:
    print(key)
# options=[input() for _ in range(n)]
# used=[input() for _ in range(n-1)]
# options.sort()
# used.sort()
# options=deque(options)
# used=deque(used)

# print(options)
# print(used)

# for x in options:
#   val=used.popleft()
#   if x!=val:
#     print(x)
#     break


  