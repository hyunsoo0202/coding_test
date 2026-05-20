import sys
sys.stdin=open('input.txt', 'rt')
n, k = map(int, input().split())

numbers = list(map(int, input().split()))
sum = set()
print(numbers);
for a in range(len(numbers)):
    for b in range(a+1,len(numbers)):
        for c in range(b+1, len(numbers)):
            
            sum.add(numbers[a] + numbers[b] + numbers[c])
sum=list(sum)
sum.sort(reverse=True)
print(sum[k-1])

