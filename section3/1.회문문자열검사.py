import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
print(n)

for i in range(n):
    str=input().lower()
    # print(str[0])
    for x in range(len(str)//2):
        if str[x]!=str[-x-1]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' %(i+1))