import sys
sys.stdin=open('input.txt', 'rt')
n=int(input())


print(n)
cn=[0]*(n+1)
cnt=0
print(cn)

for i in range(2, (n+1)):
    if cn[i]==0:
        cnt+=1
        for j in range(i, (n+1), i):
            cn[j]=1

print(cnt)



















"""
# 정답 코드
ch=[0]*(n+1)
cnt=0

for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1


print(cnt)
"""