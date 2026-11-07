class employee:
    a = 1 
    def show(self):
        print(f"the attribute of a is {self.a}")

e = employee()
e.a = 32
e.show() # this shows instance attribute

# but if we want class attribute then we had to use clsass method
class employee:
    a = 1 
    @classmethod
    def show(cls):
        print(f"the attribute of a is {cls.a}")

e = employee()
e.a = 32
e.show()
