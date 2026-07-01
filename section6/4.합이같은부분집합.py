import sys
sys.stdin=open('input.txt', 'rt')

def dfs(L, sum):
  global flag
  if sum>total//2: return
  if flag: return
  if L==n:
    if sum==(total-sum):
      print('YES')
      flag=1
  else:
    dfs(L+1, sum+arr[L])
    dfs(L+1, sum)
  



if __name__=='__main__':
  n=int(input())
  arr=list(map(int, input().split()))  
  total=sum(arr)
  flag=0
  dfs(0,0)
  if flag==0: print('NO')





















# n=int(input())
# arr=list(map(int, input().split()))

# print(arr)

# def dfs(idx):
#   global res
  
#   if idx==n:
#     if sum(a)==sum(b):
#       res='YES'
#       return
#   else:
#     a.append(arr[idx])
#     dfs(idx+1)
#     a.pop()
#     b.append(arr[idx])
#     dfs(idx+1)
#     b.pop()



# if __name__=='__main__':
#   a=[]
#   b=[]
#   idx=0
#   res='NO'
#   dfs(idx)
#   print(res)




