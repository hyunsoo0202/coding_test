import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

print(a)
print(b)

p1=0
p2=0
res=[]
# print(i,j)

for i in range(n+m):
    if a[p1]<=b[p2]:
        res.append(a[p1])
        p1+=1
    else:
        res.append(b[p2])
        p2+=1
    
    if p1==n:
        res.extend(b[p2:])
        break
    if p2==m:
        res.extend(a[p1:])
        break
print(res)


















"""
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

p1=0
p2=0
c=[]

while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
print(c)
"""

    