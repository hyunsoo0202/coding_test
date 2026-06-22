import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int, input().split())
    arr.append([a,b])

arr.sort(reverse=True)
print(arr)

largest=0
cnt=0
for x in arr:
    if x[1]>largest:
        cnt+=1
        largest=x[1]
print(cnt)
# cnt=0
# for a,b in arr:
#     print(a,b)
#     for c,d in arr:
#         if a<c and b<d:
#             break
#     else:
#         cnt+=1

# print(cnt)