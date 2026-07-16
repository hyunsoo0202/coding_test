import sys
sys.stdin=open('input.txt', 'rt')

def dfs(node):
  global cnt
  if node==5:
    cnt+=1
  else:
    for j in range(1, n+1):
      if ch[j]==0 and arr[node][j]==1:
        ch[j]=1
        dfs(j)
        ch[j]=0


if __name__=="__main__":
  n,m=map(int, input().split())

  ch=[0]*(n+1)
  arr=[[0]*(n+1) for _ in range(n+1)]
  cnt=0
  for _ in range(m):
    s,e=map(int, input().split())
    arr[s][e]=1

  ch[1]=1
  dfs(1)
  print(cnt)
  