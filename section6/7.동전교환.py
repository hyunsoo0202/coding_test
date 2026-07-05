import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=list(map(int, input().split()))
total=int(input())
min_val=2147000000
arr.sort(reverse=True)

def dfs(L, balance):
  global min_val

  if balance<0:
    return
  if min_val<L:
    return
  if balance==0:
    min_val=L
  else:
    for x in arr:
      dfs(L+1, balance-x)

dfs(0, total)
print(min_val)
