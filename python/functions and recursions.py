# def avg():
#     a=int (input("enter number"))
#     b=int (input("enter number"))
#     c=int(input("enter number"))
#     average=(a+b+c)/3
#     print(average)
# avg()
# avg()
# avg()

# functions with arguments

# def goodday(name,ending):
#     print("Good Day,"+ name)
#     print(ending)
# goodday("vaishu","Thank you!")

# factorial

def factorial(n):
    if (n==1 or n==0):
        return 1
    return n * factorial(n-1)

n=int(input("enter number"))
print(f"the factorial of this number is{factorial(n)}")