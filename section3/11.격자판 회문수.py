import sys
sys.stdin=open('input.txt', 'rt')

arr=[list(map(int, input().split())) for _ in range(7)]

cnt=0
print(arr)

# for i in range(3):
#     for j in range(7):
#         tmp1=arr[j][i:i+5]
#         if tmp1==tmp1[::-1]:
#             cnt+=1
        
for i in range(7):
    for j in range(3):
        tmp=arr[i][j:j+5]
        if tmp==tmp[::-1]:
            cnt+=1
        
        col_tmp=[arr[k][i] for k in range(j, j+5)]
        if col_tmp==col_tmp[::-1]:
            cnt+=1
print(cnt)
        
            

# for i in range(7):
#     for j in range(3):
#         tmp1=[]
#         tmp2=[]
#         for k in range(j, j+5):
#             tmp1.append(arr[i][k])
#             tmp2.append(arr[k][i])
#         if tmp1[0]==tmp1[4] and tmp1[1]==tmp1[3]:
#             cnt+=1
#         if tmp2[0]==tmp2[4] and tmp2[1]==tmp2[3]:
#             cnt+=1
