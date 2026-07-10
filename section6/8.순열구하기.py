import sys
sys.stdin=open('input.txt', 'rt')

n,m=map(int, input().split())

def dfs(L):
  global cnt
  global ch
  global res
  global arr
  if L==m:
    for x in res:
      print(x, end=' ')
    cnt+=1
    print()

  else:
    for x in arr:
      if ch[x]!=1:
        ch[x]=1
        res[L]=x
        dfs(L+1)
        ch[x]=0

if __name__=='__main__':
  cnt=0
  ch=[0]*(n+1)
  arr=[x for x in range(1, n+1)]
  res=[0]*m
  dfs(0)
  print(cnt)