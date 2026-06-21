import sys
sys.stdin=open('input.txt', 'rt')

n,m=map(int, input().split())
songs=list(map(int, input().split()))
lt=max(songs)
rt=sum(songs)
res=0


def check(size):
    cnt=1
    tot=0
    for x in songs:
        if tot+x>size:
            cnt+=1
            tot=x
        else:
            tot+=x
    return cnt

while lt<=rt:
    mid=(lt+rt)//2
    if check(mid)<=m: 
        # 3장 혹은 3장보다 적게 담을 수 있다는건 용량을 더 줄이면 더 적은 용량으로 3장에 담을 수 있다는 뜻이므로 
        # 정답 후보가 될 수 있음. 그래서 범위 중 큰 부분을 떼어내어 더 적은 최소 용량을 탐색함
        rt=mid-1
        res=mid
    elif check(mid)>m:
        lt=mid+1
    # else:
    #     res=mid
    #     break
print(res)