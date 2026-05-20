import sys
sys.stdin=open('input.txt', 'rt')

number_list=list(range(1, 21))

print(number_list)
# print(number_list[:3])
# print(number_list[1:3])
# print(number_list[10:])

for _ in range(10):
    a,b=map(int, input().split())
    for i in range((b-a+1)//2):
        number_list[a-1+i], number_list[b-1-i]=number_list[b-1-i], number_list[a-1+i]
    # # print(a,b)
    # head=number_list[:a-1]
    # mid=number_list[a-1:b]
    # mid.reverse()
    # tail=number_list[b:]
    # number_list=head+mid+tail
print(number_list)   
    