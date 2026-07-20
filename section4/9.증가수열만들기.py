import sys
sys.stdin=open('input.txt', 'rt')
from collections import deque

n=int(input())
arr=list(map(int, input().split()))

lt=0
rt=n-1
tmp=[]
res=""
min_val=0

while lt<=rt:
  if arr[lt]>min_val:
    tmp.append((arr[lt], "L"))
  if arr[rt]>min_val:
    tmp.append((arr[rt], "R"))
  if len(tmp)==0:
    break
  else:
    tmp.sort()
    res+=tmp[0][1]
    min_val=tmp[0][0]
    if tmp[0][1]=="L":
      lt+=1
    else:
      rt-=1
  tmp.clear()
print(len(res))
print(res)






























# n=int(input())
# arr=list(map(int, input().split()))
# print(arr)
# ep=0
# lt=0
# rt=n-1
# tmp=[]
# res=""

# while lt<=rt:
#     if ep<arr[lt]:
#         tmp.append((arr[lt], "L"))
#     if ep<arr[rt]:
#         tmp.append((arr[rt], "R"))
#     if len(tmp)==0:
#         break
#     else:
#         tmp.sort()
#         res+=tmp[0][1]
#         ep=tmp[0][0]
#         if tmp[0][1]=="L":
#             lt+=1
#         else:
#             rt-=1
#         tmp.clear()
# print(res)
        