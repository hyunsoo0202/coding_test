import sys
sys.stdin=open('input.txt', 'rt')

res=""
stack=[]
str=input()
print(str)


for x in str:
  if x.isdecimal():
    stack.append(x)
  else:
    if x=="(":
      stack.append(x)
    elif x=="*" or x=="/":
      while stack and (stack[-1]=="*" or stack[-1]=="/"):
        res+=stack.pop()
      stack.append(x)
    elif x=="+" or x=="-":
      while stack and stack[-1]!="(":
        res+=stack.pop()
      stack.append(x)
    elif x==")":
      while stack and stack[-1]!="(":
        res+=stack.pop()
      stack.pop()
    

while stack:
  res+=stack.pop()

print(res)

    



# for i in range(len(str)):
#   if str[i].isdecimal():
#     res+=str[i]
#   else:
#     if str[i]=="(":
#       stack.append(str[i])
#     elif str[i]=="*" or str[i]=="/":
#       while stack and (stack[-1]=="*" or stack[-1]=="/"):
#         res+=stack.pop()
#       stack.append(str[i])
#     elif str[i]=="+" or str[i]=="-":
#       while stack and stack[-1]!="(":
#         res+=stack.pop()
#       stack.append(str[i])
#     elif str[i]==")":
#       while stack and stack[-1]!="(":
#         res+=stack.pop()
#       stack.pop()

# while stack:
#   res+=stack.pop()
