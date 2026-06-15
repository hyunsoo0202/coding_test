import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
scores=list(map(int, input().split()))

print(scores)

sum=0
cnt=0
for x in scores:
    if x==0:
        cnt=0
    elif x!=0:
        cnt+=1
        sum+=cnt
print(sum)