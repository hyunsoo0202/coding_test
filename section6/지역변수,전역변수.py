def DFS1():
  print(cnt)

def DFS2():
  global cnt
  if cnt==5:
    cnt=cnt+1 
    print(cnt)

def DFS():
  global a
  a=a+[4] # 에러 발생 -> a가 지역변수가 되어버림
  print(a)
  
if __name__=='__main__':
  a=[1,2,3]
  cnt=5
  DFS1()
  DFS2()
  DFS()
  print(cnt)
  print(a)