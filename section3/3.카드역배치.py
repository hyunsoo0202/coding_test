import sys
sys.stdin=open('input.txt', 'rt')

arr=list(range(1, 21))



for _ in range(10):
    [a,b]=map(int, input().split())
    print(a,b)
    for i in range((b-a+1)//2):
        arr[a-1+i],arr[b-1-i]=arr[b-1-i],arr[a-1+i]
print(arr)



















"""
for _ in range(10):
    a,b=map(int, input().split())
    for i in range((b-a+1)//2):
        number_list[a-1+i], number_list[b-1-i]=number_list[b-1-i], number_list[a-1+i]

print(number_list)   
"""    