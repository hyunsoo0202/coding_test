import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
meetings=[]
for _ in range(n):
    s, e=map(int, input().split())
    meetings.append((s,e))


meetings.sort(key=lambda x: (x[1],x[0]))


cnt=0
et=0
for s,e in meetings:
    
    if s>=et:
        cnt+=1
        et=e
print(cnt)