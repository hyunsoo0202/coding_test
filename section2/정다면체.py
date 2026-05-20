import sys
sys.stdin=open('input.txt', 'rt')

n,m=map(int, input().split())
print(n,m)

tmp=[0]*(n+m+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        
        tmp[i+j]+=1

min_value=-2147000000
for i in tmp:
    if min_value<i:
        min_value=i
print(min_value)

for idx, val in enumerate(tmp):
    if min_value==val:
        print(idx, end=' ')


    


# for i in range(n):
#     for j in range(m):
#         print(i+1, j+1)
#         tmp[i+j+1]+=1
# print(max(tmp))

# max_value=max(tmp)
# answer=list()
# for idx, x in enumerate(tmp):
#     if x==max_value:
#         answer.append(idx+1)

# print(answer)