# greatest of three number
# def greatest(a,b,c):
    
#     if(a>b and a>c ):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
#     else:
#         print("none")

# a =int(input("enter number"))
# b =int(input("enter number"))
# c =int(input("enter number"))

# print(greatest(a,b,c))

# celcius to fahrenheit

# def  f_to_c(f):
#     return 5*(f-32)/9

# f=int(input("enter temperature"))
# c=f_to_c(f)
# print (f"{round(c , 2)}")

# print without new line

# print("a")
# print("b")
# print("c",end="")
# print("d",end="")

# recursive function to print sum of n natural numbers

# def sum(n):
#   if(n==1):
#    return 1

#   return (sum) (n-1)+n
# n=int(input("enter number"))
# print(sum(n))

'''
***
**
*
'''
# def  pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)
# n=int(input("enter number"))   
# pattern(n)

# inches to cms

# def inches_to_cms(inch):
#     return inch * 2.54
# n=int(input("enter number"))
# print (f"the value is {inches_to_cms(n)}")

# remove a given word from a list and strip at same time

# def rem(l,word):
#     n=[]
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n
# l=["harry","vaishu","gungun","rohan","shubham"]
# print(rem(l,"an"))

# multiplication table

def multiply(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
n=int(input("enter number"))
multiply(n)
