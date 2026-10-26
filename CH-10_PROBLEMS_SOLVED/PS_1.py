class programmer:
    company  = "Microsoft"
    def __init__(self,name,salary,pin,age,):
        self.name = name
        self.salary = salary
        self.pin = pin
        self.age = age

p1 = programmer("harry",1500000,12345,30,)
p2 = programmer("aayush",4000000,24680,25)
p3 = programmer("rohan",2000000,34567,29)
p4 = programmer("sohan",1000000,34567,29)
p5 = programmer("mohan",3000000,34567,27)

print(p1.name,p1.salary)
print(p2.name,p2.pin)
print(p3.salary,p3.pin)
print(p4.pin,p4.salary)
print(p5.name,p5.salary,p5.pin)

