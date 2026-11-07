class Employee:
    def __init__(self):
       print("constructor of employee")
    a = 1

class programmer(Employee):
    def __init__(self):
           print("constructor of employee")
    b = 2

class manager(programmer):
    def __init__(self):
           super().__init__()
           print("constructor of employee")
    c = 3

o = programmer()
print(o.a) # prints the attribute 
# print(o.b) # shows an error because there is no b attribute in employe class

a = manager()
print(a.a,a.b,a.c)

b = Employee()
print(b.a)