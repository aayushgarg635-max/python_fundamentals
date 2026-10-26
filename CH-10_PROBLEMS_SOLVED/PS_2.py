import math

class calculator:
    subject = "Mathematics"

    def __init__(self,n):
        self.n = n
        self.square = n * n
        self.cube = n*n*n
        self.squareroot = math.sqrt(n)

    def display(self):
        print("square:",self.square)
        print("cube",self.cube)
        print("square root",self.squareroot)

n = int(input("Enter the number: "))
c = calculator(n)
c.display()

    