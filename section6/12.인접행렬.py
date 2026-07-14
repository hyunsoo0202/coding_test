import sys
sys.stdin=open('input.txt', 'rt')

n,m=map(int, input().split())
# print(n,m)
g=[[0]*(n+1) for _ in range(n+1)]
# print(g)

for _ in range(m):
  v1,v2,r=map(int, input().split())
  g[v1][v2]=r

for i in range(1, n+1):
  for j in range(1, n+1):
    print(g[i][j], end=' ')
  print()
# print(g)
