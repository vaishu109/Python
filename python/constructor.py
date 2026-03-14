class employee:
     language="py"
     salary=1200000
     def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        
rahul=employee("rahul","1200000","javascript")
print(rahul.name,rahul.salary,rahul.language)