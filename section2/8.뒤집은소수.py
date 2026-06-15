import sys
sys.stdin=open('input.txt', 'rt')
n=int(input())
numbers=list(map(int,input().split()))

print(numbers)

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, (x//2)+1):
        if x%i==0:
            return False
    else:
        return True
    
for i in numbers:
    res=reverse(i)
    
    if isPrime(res)==True:
        print(res, end=' ')






















"""
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

# def reverse(x):
#     tmp=list(str(x))
#     tmp.reverse()
#     tmp=''.join(tmp)
#     return int(tmp)

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True


for i in numbers:
    res=reverse(i)
    if isPrime(res)==True:
        print(res, end=' ')
"""    
    

