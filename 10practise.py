class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("aastha",120000000,6785)
print(p.name,p.salary,p.pin,p.company)