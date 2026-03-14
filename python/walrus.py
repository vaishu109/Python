# # using walrus operator
# if(n := len([1,2,3,4,4]))>3:
#  print(f"list is too long ({n} elements , expected <= 3)")

# # types

# n:int=5
# def greeting(name:str)->str:
#     return f"hello,{name}!"
# print(greeting("alice"))

# # match case

# def match_case(status):
#    match status:
#       case 200:
#          return "ok"
#       case 100:
#          return "ok ok"
#       case 400:
#          return "ok ok ok"
#       case 800:
#          return "ok ok ok"
# print(match_case(200))

# # merged dictionary

# dict1={'a':1,'b':2,'c':3}
# dict2={'d':4,'e':5,'f':6}
# merged=dict1|dict2
# print(merged)

# # exception handling

# try:
#    a=int(input("enter a number:"))
# except Exception as e:
#  print(e)
# except ValueError as v:
#  print("hey")
#  print(v)

#  print("thank you")

#  try with else

# a=int(input("enter a number"))
# b=int(input("enter a number"))
# if(b==0):
#  raise ZeroDivisionError("you cannot divide by zero")
# else:
#   print(f"the division a/b is{a/b}")

# try with finally

# try:
#     a=int(input("enter number:"))
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     print("wow finally")

# enumerate

# l=[3,43,67,5,43,555,54]
# for index,item in enumerate(l):
#     print(f"the item number at index {index} is {item}")

# list comprehension

myList=[2,3,4,5,6]
# squaredList=[]
# for item in myList:
#     squaredList.append(item*item)
squaredList=[i*i for i in myList]
print(squaredList)

