import sys
sys.stdin=open('input.txt', 'rt')
n=int(input())
digits=list(map(int, input().split()))

# print(n)
print(digits)

def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

# def digit_sum(x):
#     sum=0
#     for i in str(x):
#         sum+=int(i)
#     return sum


res=0
max_val=-2147000000
for i in digits:
    
    sum=digit_sum(i)
    if max_val<sum:
        max_val=sum
        res=i
print(i)