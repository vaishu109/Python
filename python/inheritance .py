# class employee:
#     company="ITC"
#     def show(self):
#         print(f"the name of the employee is {self.name} and salary is {self.salary}")
# class programmer:
#     company="ITC Infotech"
#     def showlanguage(self):
#         print(f"the name of the employee is {self.name} and language is {self.language}")
# a=employee()
# a.name="vaishnavi"
# a.salary=1200000
# b=programmer()
# b.name="rahul"
# b.language="py"

# print(a.company,b.company,b.language)
# a.show()
# b.showlanguage()

# # # multiple inheritance

# class employee:
#     company="ITC"
#     def show(self):
#         print(f"the name of the employee is {self.name} and salary is {self.salary}")
# class coder:
#     language="python"
#     def printlanguage(self):
#       print(f"out of all languages the language is {self.language}")
# class programmer(employee,coder):
#     company="ITC Infotech"
#     def showlanguage(self):
#         print(f"the name of the employee is {self.name} and language is {self.language}")
# a=employee()
# a.name="vaishnavi"
# a.salary=1200000

# b=programmer()
# b.name="rahul"
# # b.language="py"

# # print(a.company,b.company,b.language)
# a.show()
# b.printlanguage()
# b.showlanguage()

# # #multilevel inheritance

# class employee:
#     a=1
# class programmer(employee):
#     b=2
# class manager(programmer):
#     c=3
# o=employee()
# print(o.a)
# o=programmer()
# print(o.a,o.b)
# o=manager()
# print(o.a,o.b,o.c)

# # super

# class employee:
#     def __init__(self):
#         print("constructor of employee")
#     a=1
# class programmer(employee):
#     def __init__(self):
#         print("constructor of programmer")
#     b=2
# class manager(programmer):
#     def __init__(self):
#          super().__init__()
#          print("constructor of manager")
#     c=3
# # o=employee()
# # print(o.a)
# # o=programmer()
# # print(o.a,o.b)
# o=manager()
# print(o.a,o.b,o.c)


# # class method

# class employee:
#     a=1
#     @classmethod
#     def show(cls):
#         print(f"the class attribute of a is {cls.a}")
# e=employee()
# e.a=45
# e.show()

# #property decorator

class employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name (self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
e=employee()
e.a=45
e.name ="Vaishnavi Shaw"
print(e.name)
e.show()
