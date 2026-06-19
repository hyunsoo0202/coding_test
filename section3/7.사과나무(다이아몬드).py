import sys
sys.stdin=open('input.txt', 'rt')


n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]

print(arr)

tot=0
p1=n//2
p2=n//2

print(p1, p2)
for i in range(n):
    for j in range(p1, p2+1):
        tot+=arr[i][j]
    if i<(n//2):
        p1-=1
        p2+=1
    else:
        p1+=1
        p2-=1
print(tot)
































"""
n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
print(arr)

s=e=n//2
res=0
for i in range(n):
    for j in range(s, e+1):
        res+=arr[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
"""