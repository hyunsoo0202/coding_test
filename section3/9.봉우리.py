import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
arr=[list(map(int, input().split())) for i in range(n)]
direct=[[-1,0],[1,0],[0,-1],[0,1]]
cnt=0
for i in range(n):
    for j in range(n):

        for [dx, dy] in direct:
            x=i+dx  
            y=j+dy

            if x<0 or x>n-1 or y<0 or y>n-1:
                continue
            if arr[i][j]<arr[x][y]:
                break
        else:
            cnt+=1

print(cnt)

# for [dx,dy] in direct:
#     print(dx, dy)




















"""
n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]

print(arr)
cnt=0
dx=[-1,0,1,0]
dy=[0,-1,0,1]
di=[[0,1],[0,-1],[-1,0],[1,0]]

for i in range(n):
    for j in range(n):

        for k in range(4):
            x=i+dx[k]
            y=j+dy[k]

            if (x>=0 and x<=(n-1) and y>=0 and y<=(n-1)):
                if (arr[i][j]<=arr[x][y]):
                    break
        else:
            cnt+=1
        # tmp=False
        # for k in di:
        #     x=i+k[0]
        #     y=j+k[1]

        #     if (x>=0 and x<=n-1 and y>=0 and y<=n-1):
        #         if (arr[i][j]<=arr[x][y]):
        #             tmp=True
        
        # if tmp==False:
        #     cnt+=1
        
        #i,j+1 #상
        #i,j-1 #하
        #i-1,j #좌
        #i+1,j #우
print(cnt)
"""