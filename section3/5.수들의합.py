import sys
sys.stdin=open('input.txt', 'rt')

[n,m]=map(int,input().split())
arr=list(map(int, input().split()))

lt=0
rt=0
cnt=0
tot=0

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

    

# while r<n:
#     sum=0
#     for i in range(l, r+1):
#         sum+=arr[i]
    
#     if sum<m:
#         r+=1
#     elif sum==m:
#         cnt+=1
#         l+=1
#     else:
#         l+=1
# print(cnt)





























"""
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
"""
