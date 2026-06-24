import sys
sys.stdin=open('input.txt', 'rt')

arr=input()
print(arr)

prev=''
tot=0
stack=[]

for i in range(len(arr)):
  if arr[i]=='(':
    stack.append(arr[i])
  else:
    if arr[i-1]=='(':
      stack.pop()
      tot+=len(stack)
    else:
      stack.pop()
      tot+=1
print(tot)
