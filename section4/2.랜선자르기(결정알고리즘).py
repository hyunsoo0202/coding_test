import sys
sys.stdin=open('input.txt', 'rt')

k, n=map(int, input().split())
line=[]
res=0 # 최대값
largest=0

for _ in range(k):
    item=int(input())
    line.append(item)
    largest=max(largest, item)

lt=0
rt=largest

def count(len):
    cnt=0
    for i in line:
        cnt+=(i//len)
    return cnt

while lt<=rt:
    mid=(lt+rt)//2

    if count(mid)<n:
        rt=mid-1
    else:
        res=mid
        lt=mid+1

print(res)
