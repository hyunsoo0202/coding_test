# print("Hllo, Python!")

# name = "철수"
# age = 25
# print(f"이름: {name}, 나이: {age}")

# a=1
# A=2

# A1=3
# print(a, A, A1)
# a, b, c=3, 2, 1
# print(a, b, c)

# 값 교환
# a, b = 10, 20
# print(a, b)
# a, b = b, a

# 변수 타입
# a = 12345
# print(type(a))
# a = 12.12345
# print(type(a))
# a = 'student'
# print(a)

# 출력방식
# print("number")
# a, b, c = 1, 2, 3
# print(a, b, c)
# print("number:", a, b, c)
# print(a, b, c, sep='\n')
# print(a, end = ' ')
# print(b, end = ' ')
# print(c)

# a, b = map(int, input("숫자를 입력하세요 : ").split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

# a=4.3
# b=5
# c=a+b
# print(type(c))

# 조건문 if
# x=10        
# if x>0:
#     if x<10:
#         print("10보다 작은 자연수")           

# x=7
# if x>0 and x<10:
#     print("10보다 작은 자연수")

# x=7
# if 0<x<10:
#     print("10보다 작은 자연수")

# 분기문
# x=-3
# if x>0:
#     print("양수")
# else:
#     print("음수")

# 다중 if 문
# x=93
# if x>=90:
#     print("A")
# elif x>=80:
#     print("B")
# elif x>=70:
#     print("C")
# elif x>=60:
#     print("D")
# else:
#     print("F")

# 반복문
# a=range(1, 11) # 1~10까지 정수를 만듦
# print(a)
# print(list(a))

# for i in range(1, 11): # i가 0~9까지 돌면서 반복
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

# while
# i=1
# while i<=10:
#     print(i)
#     i=i+1

# i=10
# while i>=1:
#     print(i)
#     i=i-1

# break
# i=1
# while True:
#     print(i)
#     if i==10:
#         break
#     i+=1

# continue
# for i in range(1, 11):
#     if i%2==0: # 짝수
#         continue # 다음 구문은 실행 X
#     print(i)

# for - else
# for i in range(1, 11):
#     print(i)
#     if i>15:
#         break
# else:
#     print(11)

# 문제 풀이 

# 1부터 N까지 홀수 출력하기

# n=int(input())
# for i in range(1, n+1):
#     if i%2==1:
#         print(i)

# 1부터 N까지의 합 구하기
# n=int(input())
# sum=0
# for i in range(1, n+1):
#     sum+=i
# print(sum)

# N의 약수 출력하기
# n=int(input())
# for i in range(1, n+1):
#     if n%i==0:
#         print(i, end=' ')

# 중첩 반복문
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=' ')
#     print()

# 문자열과 내장함수 
# msg="It is Time"
# print(msg.upper())
# print(msg.lower())
# print(msg)
# tmp=msg.upper()
# print(tmp)
# print(tmp.find('T'))
# print(tmp.count('T'))
# print(msg)
# print(msg[:2]) # slice
# print(msg[3:5])
# print(len(msg))

# for i in range(len(msg)):
#     print(msg[i], end=' ')
# print()

# for x in msg:
#     print(x, end='')
# print()

# for x in msg:
#     if x.isalpha():
#         print(x, end='')
# print()

# tmp='AZ'
# for x in tmp:
#     print(ord(x)) # 아스키 넘버

# tmp='az'
# for x in tmp:
#     print(ord(x))

# tmp=65
# print(chr(tmp))

# 리스트와 내장함수
# a=[]
# # print(a)
# b=list()
# # print(b)

# a=[1, 2, 3, 4, 5]
# # print(a)
# # print(a[0])
# b=list(range(1, 11))
# # print(b)
# c=a+b
# # print(c)

# a.append(6)
# print(a)
# a.insert(3, 7)
# print(a)
# a.pop()
# print(a)
# a.pop(3)
# print(a)
# a.remove(4)
# print(a)
# print(a.index(5))

# a=list(range(1, 11))
# print(a)
# print(sum(a))
# print(max(a))
# print(min(a))

# import random as r
# r.shuffle(a)
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.clear()
# print(a)

# a=[23, 12, 36, 53, 19]
# print(a[:3])
# print(a[1:4])
# print(len(a))

# for i in range(len(a)):
#     print(a[i], end=' ')
# print()

# for x in a:
#     print(x)
# print()

# for x in enumerate(a):
#     print(x)

# b=(1, 2, 3, 4, 5) # 튜플 -> 요소 변경 불가
# print(b)

# for x in enumerate(a):
#     print(x[0], x[1])
# print()

# for index, value in enumerate(a):
#     print('index: ', index)
#     print('value: ', value)
# print()

# if all(50>x for x in a):
#     print('YES')
# else:
#     print('NO')


# if any(15>x for x in a): # 한번이라도 참이 있으면 참
#     print('YES')
# else:
#     print('NO')   

# a=[0]*10 # [0, 0, 0, 0 ..., 0]
# print(a)

# 2차원 리스트
# a=[[0]*3 for _ in range(3)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# a[0][1]=1
# print(a)
# a[1][1]=2
# print(a)

# for x in a:
#     print(x)

# for x in a:
#     for y in x:
#         print(y, end=' ')
#     print()

# 함수 만들기
# def add(a, b):
#     c=a+b
#     print(c)

# add(3, 2)
# add(5, 7)

# def add(a, b):
#     c=a+b
#     return c

# result=add(3, 2)
# print(result)

# def add(a, b):
#     c=a+b
#     d=a-b
#     return c, d
# print(add(3, 2))

# def isPrime(x):
#     for i in range(2, x):
#         if x%i==0:
#             return False
#     return True    

# a=[12, 13, 7, 9, 19]

# for i in a:
#     if isPrime(i) == True:
#         print(i, end=' ')

# 람다 함수 (익명 함수, 람다 표현식)
def plus_one(x):
    return x+1
# print(plus_one(2))

# plus_two=lambda x: x+2 # << 람다 함수 << 변수에 할당을 해줘야 함.
# print(plus_two(1))

a=[1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x:x+1, a)))
