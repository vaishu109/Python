class employee:
     language="py"
     salary=1200000
     def getinfo(self):
             print(f"the language is{self.language}.the salary is {self.salary}.")
     @staticmethod
     def greet():
               print("good morning")
rahul=employee()
rahul.getinfo()
rahul.greet()