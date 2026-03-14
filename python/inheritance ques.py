# class twoDvector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"the vector is {self.i}i + {self.j}j")
# class threeDvector(twoDvector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
#     def show(self):
#         print(f"the vector is {self.i}i + {self.j}j + {self.k}k")
# a=twoDvector(1,2)
# a.show()
# b=threeDvector(1,4,6)
# b.show()

# #2

# class animals():
#     pass
# class pets(animals):
#     pass
# class dog(pets):
#     @staticmethod
#     def bark():
#         print("bow bow!")
# d=dog()
# d.bark()

# #3

# class employee:
#     salary=234
#     increment=20
#     @property
#     def salaryAfterincrement(self):
#         return(self.salary+self.salary*(self.increment/100))
#     @salaryAfterincrement.setter
#     def salaryAfterincrement(self,salary):
#         self.increment=((salary/self.salary)-1)*100
# e=employee()
# e.salaryAfterincrement=280.8
# print(e.increment)