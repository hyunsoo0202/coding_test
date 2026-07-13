import sys
sys.stdin=open('input.txt', 'rt')

def dfs(L, start_idx):
  global cnt
  if L==m:
    cnt+=1
    for x in res:
      print(x, end=' ')
    print()
  else:
    for i in range(start_idx, n+1):
      res[L]=i
      dfs(L+1, i+1)
    

if __name__=='__main__':
  n,m=map(int, input().split())
  
  res=[0]*m
  cnt=0
  print(n,m)
  dfs(0, 1)
  print(cnt)