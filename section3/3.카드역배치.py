import sys
sys.stdin=open('input.txt', 'rt')

number_list=list(range(1, 21))

print(number_list)


for _ in range(10):
    a,b=map(int, input().split())
    for i in range((b-a+1)//2):
        number_list[a-1+i], number_list[b-1-i]=number_list[b-1-i], number_list[a-1+i]

print(number_list)   
    