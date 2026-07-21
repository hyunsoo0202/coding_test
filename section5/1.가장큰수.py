import sys
sys.stdin=open('input.txt', 'rt')

n,m=map(int, input().split())
arr=[int(x) for x in str(n)]
stack=[]

for x in arr:
  while m>0 and stack and stack[-1]<x:
    stack.pop()
    m-=1
  stack.append(x)
  
if m>0:
  stack=stack[:-m]
for x in stack:
  print(x, end='')
  

































# arr,cnt=map(int, input().split())

# print(type(arr))
# arr=list(map(int, str(arr)))
# print(arr)
# # print(n)

# stack=[]
# for x in arr:
#   while stack and cnt>0 and stack[-1]<x:
#     stack.pop()
#     cnt-=1
#   stack.append(x)


# if cnt!=0:
#   stack=stack[:-cnt]
# print("".join(map(str,stack)))      
      
    
# for _ in range(n):
#   largest=0
#   for i in range(len(arr)):
#     tmp=arr.copy()
#     tmp.pop(i)
#     result=int("".join(map(str, tmp)))
#     if largest<result:
#       largest=result
#   arr=list(str(largest))
  
# print(largest)