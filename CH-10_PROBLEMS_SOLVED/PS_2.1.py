class calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square of the number is {self.n*self.n}")

    def cube (self):
            print(f"The cube of the number is {self.n*self.n*self.n}")

    def squareroot(self):
            print(f"The square root of the number is {self.n**1/2}")

a = calculator(5)
a.square()
a.cube()
a.squareroot()
b = calculator(9)
b.square()
b.cube()
b.squareroot()
