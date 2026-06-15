import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
print(n)

for i in range(n):
    str=input()
    low_str=str.lower()
    # print(low_str)

    for j in range(0, (len(low_str)//2)+1):
        if low_str[j]!=low_str[-j-1]:
            print(f"#{i+1} NO")
            break
    else:
        print(f"#{i+1} YES")
    



























"""
for i in range(n):
    str=input().lower()
    # print(str[0])
    for x in range(len(str)//2):
        if str[x]!=str[-x-1]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' %(i+1))
"""