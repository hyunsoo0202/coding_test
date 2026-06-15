import sys
sys.stdin=open('input.txt', 'rt')
n=int(input())


ch=[0]*(n+1)
cnt=0

for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1


print(cnt)

# cnt=0
# for x in range(2,n+1):
#     # print(x)
#     for i in range(2, x):
#         if x%i==0:
#             break
#     else:
#         cnt+=1
            
# print(cnt)