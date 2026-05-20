import sys
sys.stdin=open('input.txt', 'rt')

n=int(input())
scores=list(map(int, input().split()))

avg=round(sum(scores)/n)
min=2147000000
student=0
tmp_score=0

for idx, score in enumerate(scores):
    
    tmp=abs(avg-score)
    print(tmp)
    if tmp<min:
        min=tmp # 1
        student=idx+1 # 2
        tmp_score=score # 73
    elif tmp==min:
        if tmp_score<score:
            student=idx+1
            tmp_score=score
print(avg, student)
    


# a=list()
# for idx, x in enumerate(scores):
#     print(idx, x)
#     tmp=abs(avg - x)
#     if tmp<min:
#         min=tmp
#         score=x
#         res=idx+1
#     elif tmp==min:
#         if x>score:
#             score=x
#             res=idx+1
# print(avg, res)
   