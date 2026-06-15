import sys
sys.stdin=open('input.txt', 'rt')

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
