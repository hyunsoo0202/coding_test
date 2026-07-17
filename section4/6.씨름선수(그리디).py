import sys
sys.stdin=open('input.txt', 'rt')

n=int(input()) # 지원자 수

arr=[list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x:x[1], reverse=True)
# arr.sort(reverse=True)
print(arr)

largest=0
cnt=0
for i in range(n):
  if largest<arr[i][0]:
    largest=arr[i][0]
    cnt+=1

print(cnt)
  























# n=int(input())
# arr=[]
# for _ in range(n):
#     a,b=map(int, input().split())
#     arr.append([a,b])

# arr.sort(reverse=True)
# print(arr)

# largest=0
# cnt=0
# for x in arr:
#     if x[1]>largest:
#         cnt+=1
#         largest=x[1]
# print(cnt)
