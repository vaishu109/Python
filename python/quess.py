# table using for loop

# n=int(input("enter number"))
# for i in range(1,11):
#     print(f"{n} x {i}={n *i}")

    # greet names  with s

# l=["harry","rahul","soham","sohail"]
# for name in l:
#         if (name.startswith("s")):
#             print(f"hello {name}")

# print table using while loop

# n=int(input("enter number"))
# i=1
# while(i<11):
#     print(f"{n}x{i}={n*i}")
#     i+=1

# prime or not

# n=int(input("enter number"))
# if n<=2:
#     print("not prime")
# for i in range(2,   n):
#     if(n%i)==0:
#         print("number is not prime")
#         break
#     else:
#         print("number is prime")

# sum of n natural numbers

# n=int (input("enter number"))
# i=1
# sum=0
# while(i<=n):
#     sum += i
#     i += 1
# print(sum)

# factorial

# n=int (input("enter number"))
# product=1
# for i in range(1,n+1):
#     product*=i
# print(f"the factorial of{n}is {product}")

'''
  *
 ***
*****
'''
# n=int(input("enter number"))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

'''
*
**
***
'''

# n=int(input("enter number"))
# for i in range(1,n+1):
#     print("*"*i,end="")
#     print("")

'''
***
* *
***
'''
# n=int(input("enter number"))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#        print("*"* n,end="")
#     else:
#        print("*", end="")
#        print(" "*(n-2),end="")
#        print("*", end="")
#     print("")

    # reverse order  table

n=int(input("enter number"))
for i in range(1,11):
    print(f"{n}x{11-i}={n*(11-i)}")