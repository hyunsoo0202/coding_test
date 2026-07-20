import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=list(map(int, input().split()))
ch=[0]*n
print(arr)

for i in range(n):
  cur_val=i+1
  cnt=arr[i]

  for j in range(n):
    if cnt==0 and ch[j]==0:
      ch[j]=cur_val
      break
    elif ch[j]==0:
      cnt-=1
for x in ch:
  print(x, end=' ')
























# n=int(input())
# arr=list(map(int, input().split()))

# print(arr)

# tmp=[0]*n
# for i in range(n):
#     cnt=arr[i]
#     number=i+1
#     for j in range(n):
#         if cnt==0 and tmp[j]==0:
#             tmp[j]=number
#             break    
#             # if tmp[j]!=0:
#             #     continue
#             # else:
#             #     tmp[j]=number
#             #     break
#         elif tmp[j]==0:
#             cnt-=1
#             continue

# print(tmp)
