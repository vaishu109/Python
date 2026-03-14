# #class storing programmer info
# class programmer:
#     company="microsoft"
#     def __init__ (self,name,salary,pin):
#         self.name=name 
#         self.salary=salary
#         self.pin=pin
# p=programmer("rahul",1200000,743201)
# print(p.name,p.company,p.salary,p.pin)
# r=programmer("vaishnavi",1200000,743551)
# print(r.name,r.company,r.salary,r.pin)
# q=programmer("gungun",1000000,743301)
# print(q.name,q.company,q.salary,q.pin)
       
# #class "calculator finds square cube of a no"

# class calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"the square is {self.n*self.n}")
#     def cube(self):
#         print(f"the cubeis {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"the square root is {self.n**1/2}")   

# a=calculator(4)
# a.square()
# a.cube()
# a.squareroot()

# #create class with a class attribute a create an object and set a

# class demo:
#  a=4
# o=demo()
# print(o.a)
# o.a=0
# print(o.a)
# print(demo.a)

# #use static method
# class calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"the square is {self.n*self.n}")
#     def cube(self):
#         print(f"the cubeis {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"the square root is {self.n**1/2}")   
#     @staticmethod
#     def hello():
#       print("hello")
# a=calculator(4)
# a.hello()
# a.square()
# a.cube()
# a.squareroot()

# # claa train which has methods to book a ticket,get status,get fare information of train running
# from random import randint
# class train:
#         def __init__(self,trainNo):
#             self.trainNo=trainNo
#         def book(self,fro,to):
#               print(f"ticket is booked in train no {self.trainNo} from {fro} to {to}")
#         def getstatus(self):
#               print(f"train no {self.trainNo} is running on time")
#         def getfare(self,fro,to):
#               print(f"ticket fare in train no {self.trainNo} from {fro} to {to} is{randint(222,5555)}")
# t=train(12678)
# t.book("Rampur","Delhi")
# t.getstatus()
# t.getfare("Rampur","Delhi")

# #chnge the self parameter inside class

from random import randint
class train:
        def __init__(slf,trainNo):
            slf.trainNo=trainNo
        def book(slf,fro,to):
              print(f"ticket is booked in train no {slf.trainNo} from {fro} to {to}")
        def getstatus(slf):
              print(f"train no {slf.trainNo} is running on time")
        def getfare(slf,fro,to):
              print(f"ticket fare in train no {slf.trainNo} from {fro} to {to} is{randint(222,5555)}")
t=train(12678)
t.book("Rampur","Delhi")
t.getstatus()
t.getfare("Rampur","Delhi")