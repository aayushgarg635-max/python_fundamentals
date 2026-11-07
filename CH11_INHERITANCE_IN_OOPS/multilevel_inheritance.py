class Employee:
    a = 1

class programmer(Employee):
    b = 2

class manager(programmer):
    c = 3

o = programmer()
print(o.a) # prints the attribute 
# print(o.b) # shows an error because there is no b attribute in employe class

a = manager()
print(a.a,a.b,a.c)

b = Employee()
print(b.a)