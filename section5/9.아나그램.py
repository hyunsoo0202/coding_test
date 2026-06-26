import sys
sys.stdin=open('input.txt', 'rt')

str1=input()
str2=input()

# print(str1, str2)
d1=dict()
# d2=dict()

for x in str1:
  d1[x]=d1.get(x,0)+1

for x in str2:
  d1[x]=d1.get(x,0)-1

# for x in str2:
#   d2[x]=d2.get(x,0)+1

for x in d1.values():
  if x!=0:
    print('NO')
    break
else:
  print('YES')
# print(d1)

# print(d1.keys())

# for i in d1.keys():
#   print(i)
#   if i in d2.keys():
#     if d1[i]!=d2[i]:
#       print('NO')
#       break
#   else:
#     print('NO')
#     break
# else:
#   print('YES')



