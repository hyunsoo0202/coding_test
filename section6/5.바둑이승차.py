import sys
sys.stdin=open('input.txt', 'rt')

c,n=map(int, input().split())
arr=[int(input()) for _ in range(n)]
total=sum(arr)
result=-2147000000

def dfs(L, sub_total, tsum):
  global result
  if sub_total+(total-tsum)<result:
    return
  if sub_total>c:
    return
  if L==n:
    if sub_total>result:
      result=sub_total
  else:
    dfs(L+1, sub_total+arr[L], tsum+arr[L])
    dfs(L+1, sub_total, tsum+arr[L])

dfs(0,0,0)
print(result)




















# c,n=map(int, input().split())
# arr=[int(input()) for _ in range(n)]
# print(c,n)
# print(arr)

# sum_list=[]

# def dfs(L, sub_total):
#   if sub_total>c:
#     sum_list.append(sub_total-arr[L-1])
#     return
#   elif L==n:
#     sum_list.append(sub_total)
#     return
#   else:
#     dfs(L+1, sub_total+arr[L])
#     dfs(L+1, sub_total)
    
# dfs(0,0)
# print(sum(arr)-81)
# print(max(sum_list))