import sys
from collections import deque

sys.stdin=open('input.txt', 'rt')

n,m=map(int, input().split())
arr=list(map(int, input().split()))

arr.sort()
arr=deque(arr)
cnt=0
print(arr)
while arr:
    if len(arr)==1:
        cnt+=1
        break
    if arr[0]+arr[-1]>140:
        arr.pop()
        cnt+=1
    if arr[0]+arr[-1]<=140:
        arr.popleft()
        arr.pop()
        cnt+=1
# lt=0
# rt=n-1
# cnt=0
# while lt<=rt:
#     if arr[rt]<=140-arr[lt]:
#         rt-=1
#         lt+=1
#         cnt+=1
#     else:
#         rt-=1
#         cnt+=1

print(cnt)