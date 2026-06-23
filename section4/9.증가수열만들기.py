import sys
from collections import deque

sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=list(map(int, input().split()))
print(arr)
ep=0
lt=0
rt=n-1
tmp=[]
res=""

while lt<=rt:
    if ep<arr[lt]:
        tmp.append((arr[lt], "L"))
    if ep<arr[rt]:
        tmp.append((arr[rt], "R"))
    if len(tmp)==0:
        break
    else:
        tmp.sort()
        res+=tmp[0][1]
        ep=tmp[0][0]
        if tmp[0][1]=="L":
            lt+=1
        else:
            rt-=1
        tmp.clear()
print(res)
        