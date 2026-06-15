import sys
sys.stdin=open('input.txt', 'rt')

T=int(input())
# print(T)

for t in range(T):
    n,s,e,k = map(int, input().split())
    # print(n,s,e,k)
    numbers = list(map(int, input().split()))
    sliced = numbers[s-1:e]
    sliced.sort()
    # print(sliced)
    
    print('#%d %d' %(t+1, sliced[k-1]))
    
    