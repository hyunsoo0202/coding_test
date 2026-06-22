import sys
sys.stdin=open('input.txt', 'rt')

n,c=map(int, input().split())

cord=[]
for _ in range(n):
    cord.append(int(input()))
cord.sort()

lt=1
rt=max(cord)-min(cord)
res=0
def check(len):
    cnt=1
    ep=cord[0]    
    for i in range(1, n):
        if cord[i]-ep>=len:
            cnt+=1
            ep=cord[i]
    return cnt

while lt<=rt:
    mid=(lt+rt)//2
    if check(mid)<c:
        # 말들 사이의 거리가 너무 멀기 때문에 말을 다 배치 못한것
        # 거리를 줄여야함

        rt=mid-1
    elif check(mid)>=c:
        res=mid
        lt=mid+1
        # 말들 사이 거리가 너무 가깝기 때문에 말을 c 마리 이상 배치 가능한 것
        # 거리를 늘려야함
        # 혹은 c 마리보다 더 배치할 수 있는 말들 사이의 거리라면
        # 이것 또한 정답이 될 수는 있음 
        # -> 3마리를 배치해야 하는데 4마리를 배치할 수 있는 상황이라는건 3마리 배치도 가능한 거리이기 때문
print(mid)

