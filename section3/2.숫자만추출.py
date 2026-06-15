import sys
sys.stdin=open('input.txt', 'rt')

n=input()

res=""
for i in n:
    if i.isdecimal()==True:
        res+=i

res=int(res)
cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1

print(res)
print(cnt)



    # res=""
    # if str.isdecimal(n[i])==True:
    #     res+=n[i]

    # print(int(res))
    
    













"""
res=0
for i in n:
    if i.isdecimal():
        res=res*10+int(i)



cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(res)        
print(cnt)
    """