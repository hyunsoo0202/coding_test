import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=[list(map(int, input().split())) for i in range(n)]
m=int(input())

for i in range(m):
    [row, d, cnt]=map(int, input().split())
    print(row, d, cnt)
    target=arr[row-1]
    if d==0:
        for j in range(cnt):
            target.append(target.pop(0))
    elif d==1:
        for j in range(cnt):
            target.insert(0, target.pop())

print(arr)

tot=0
p1=0
p2=n-1
for i in range(n):
    for j in range(p1, p2+1):
        tot+=arr[i][j]
    if i<n//2:
        p1+=1
        p2-=1
    elif i>=n//2:
        p1-=1
        p2+=1
print(tot)




















"""
n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
m=int(input())



for _ in range(m):
    row_num,direction,cnt=map(int, input().split())
    for _ in range(cnt):
        if direction==0: # 왼쪽
            row=arr[row_num-1]
            val=row.pop(0)
            row.append(val)
        elif direction==1: # 오른쪽
            row=arr[row_num-1]
            val=row.pop()
            row.insert(0, val)

s=0
e=n
sum=0
for i in range(n):
    for j in range(s, e):
        sum+=arr[i][j]
    if i<n//2:
        s+=1
        e-=1
    elif i>=n//2:
        s-=1
        e+=1
print(sum)
"""