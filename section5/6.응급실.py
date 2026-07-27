import sys
sys.stdin=open('input.txt', 'rt')

from collections import deque

n,m=map(int, input().split())
arr=list(map(int, input().split()))
dq=deque([(idx, x) for (idx,x) in enumerate(arr)])
print(dq)

cnt=0

while True:
  target=dq.popleft()

  if any(target[1]<i[1] for i in dq):
    dq.append(target)
  else:
    cnt+=1
    if target[0]==m:
      break
print(cnt)


# while True:
#   target=dq[0]
#   for i in range(1, len(dq)):
#     if target[1]<dq[i][1]:
#       dq.rotate(-1)
#       break
#   else:
#     res=dq.popleft()
#     cnt+=1
#     if (res[0]==m):
#       break
# print(cnt)






























# n,m=map(int, input().split())
# arr=[(x, idx) for idx, x in enumerate(list(map(int, input().split())))]
# # print(arr)
# queue=deque(arr)
# # print(queue)

# cnt=0


# while True:
#   # print(queue)
#   x=queue.popleft()  

#   if any(x[0]<i[0] for i in queue):
#     queue.append(x)
#   else:
#     cnt+=1
#     if x[1]==m:
#       break

  # for y in queue:
    
  #   if x[0]<y[0]:
  #     queue.append(x)
  #     break
  # else:
  #   cnt+=1
  #   if x[1]==m:
  #     break
      
# print(cnt)



