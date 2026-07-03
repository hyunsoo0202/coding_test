import sys
sys.stdin=open('input.txt', 'rt')

n,m=map(int, input().split())
# print(n,m)
arr=[i for i in range(1, n+1)]

# print(arr)
res=[0]*m
cnt=0
# print(res)

def dfs(L):
  global cnt
  if L==m:
    print(str(res))
    cnt+=1
    return
  else:
    for x in arr:
      res[L]=x
      dfs(L+1)

dfs(0)
print(cnt)