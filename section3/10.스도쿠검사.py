import sys
sys.stdin=open('input.txt', 'rt')

arr=[list(map(int, input().split())) for _ in range(9)]
# print(arr)

# 행, 열 스도쿠 검사
def check():  
    for i in range(9):
        row=[0]*9
        column=[0]*9
        for j in range(9):
            row[arr[i][j]-1]=1
            column[arr[j][i]-1]=1
        
        if sum(row)!=9 or sum(column)!=9:
            return False

    # 3X3 사각형 스도쿠 검사
    for i in range(3):
        for j in range(3):
            rect=[0]*9
            for x in range(3):
                for y in range(3):
                    rect[arr[i*3+x][j*3+y]-1]=1

            if sum(rect)!=9:
                return False
    return True
        
if check():
    print('YES')
else:
    print('NO')
  

   


























# arr=[list(map(int, input().split())) for _ in range(9)]

# def check(arr):

#     for i in range(9):
#         ch1=[0]*10
#         ch2=[0]*10
#         for j in range(9):
#             ch1[arr[i][j]]=1
#             ch2[arr[j][i]]=1
#         if sum(ch1)!=9 or sum(ch2)!=9:
#             return False
    
    
#     for i in range(3):
#         for j in range(3):
            
#             ch3=[0]*10

#             for k in range(3):
#                 for s in range(3):
#                     ch3[arr[i*3+k][j*3+s]]=1
#             if sum(ch3)!=9:
#                 return False
#     return True


# if check(arr):
#     print("YES")
# else:
#     print("NO")