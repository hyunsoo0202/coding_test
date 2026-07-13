import sys
sys.stdin=open('input.txt', 'rt')

n,f=map(int, input().split())
print(n,f)

def factorial(n):
  result=1
  for i in range(1, n+1):
    result*=i
  return result

def dfs(L):
  
  if L==n:
    result=0
    for i in range(n):
      result+=res[i]*combi[i]
    
    if result==f:
      for x in res:
        print(x, end=' ')
      sys.exit(0)
  else:
    for i in range(1, n+1):
      if ch[i]==0:
        ch[i]=1
        res[L]=i
        dfs(L+1)
        ch[i]=0


if __name__=='__main__':
  combi=[0]*n
  for i in range(n):
    combi[i]=factorial(n-1)//(factorial(i)*factorial(n-1-i))

  print(combi)

  ch=[0]*(n+1)
  res=[0]*n
  
  dfs(0)