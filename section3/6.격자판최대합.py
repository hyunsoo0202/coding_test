import sys
sys.stdin=open('input.txt', 'rt')


n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]

print(arr)
max_val=-2147000000

for i in range(n):
    sum1=0
    sum2=0
    for j in range(n):
        sum1+=arr[i][j]
        sum2+=arr[j][i]
    if max_val<sum1:
        max_val=sum1
    if max_val<sum2:
        max_val=sum2

sum3=0
sum4=0
for i in range(n):
    sum3+=arr[i][i]
    sum4+=arr[i][n-1-i]
    
if max_val<sum3:
    max_val=sum3

print(max_val)














































"""
max=-2147000000

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]



for i in range(n):
    sum=0
    sum3=0
    for j in range(n):
        sum+=arr[i][j]
        sum3=arr[j][i]
    if max<sum:
        max=sum
    if max<sum3:
        max=sum3



sum1=0
sum2=0
for i in range(n):
    sum1+=arr[i][i]
    sum2+=arr[i][n-i-1]

if sum1>max:
    max=sum1
if sum2>max:
    max=sum2

print(max)
"""