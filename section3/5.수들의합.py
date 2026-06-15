import sys
sys.stdin=open('input.txt', 'rt')

n,m=map(int,input().split())
print(n,m)
arr=list(map(int,input().split()))

print(arr)


lt=0
rt=0
tot=0
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=arr[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=arr[lt]
        lt+=1
    elif tot>m:
        tot-=arr[lt]
        lt+=1
print(cnt)


# cnt=0
# for i in range(n):
#     for j in range(i, n):
        
#         res=sum(arr[i:j+1])
#         if res==m:
#             cnt+=1
#             break
#         elif res>m:
#             break
# print(cnt)
        
