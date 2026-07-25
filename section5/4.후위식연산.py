import sys
sys.stdin=open('input.txt', 'rt')

arr=input()
print(arr)
stack=[]
for x in arr:
  if x.isdecimal():
    stack.append(x)
  else:
    num1=int(stack.pop())
    num2=int(stack.pop())

    if x=="+":
      stack.append(num2+num1)
    elif x=="-":
      stack.append(num2-num1)
    elif x=="*":
      stack.append(num2*num1)
    elif x=="/":
      stack.append(num2/num1)
print(stack[0])































# a=input()
# stack=[]
# res=0

# for x in a:
#   if x.isdecimal():
#     stack.append(int(x))
#   else: 
#     target1=0
#     target2=0
    
#     target2=stack.pop()
#     target1=stack.pop()
    
#     if x=='+':
#       stack.append(int(target1)+int(target2))
#     elif x=='-':
#       stack.append(int(target1)-int(target2))
#     elif x=='*':
#       stack.append(int(target1)*int(target2))
#     elif x=='/':
#       stack.append(int(target1)/int(target2))

# print(stack[0])

"""
- 숫자 -> stack에 append
- 연산자
  - stack.pop(): 두번째 피연산자
  - stack.pop(): 첫번째 피연산자
  - 계산 후 stack에 append
- 반복문 끝나고 stack에 있는 값 출력
"""