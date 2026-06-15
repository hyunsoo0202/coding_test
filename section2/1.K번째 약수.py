import sys
sys.stdin=open('input.txt', 'rt')

n,k=map(int, input().split())
print(n, k)

# result=[]
# for x in range(1, n+1):
#     if n%x==0:
#         result.append(x)
# print(result)
# if len(result) >= k:
#     print(result[k-1])
# else:
#     print(-1)



cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
