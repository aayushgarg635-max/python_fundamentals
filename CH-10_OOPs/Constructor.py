class Employee:
    language = "python" # This is a class attribute
    salary = 1000000

    def __init__(self,name,salary,language): # dunder method which are automaticallu called
        self.name = name
        self.salary = salary
        self.language = language
        print(" I am creating an object ")

    def getinfo(self):
        print(f"the langauge is {self.language}. the salary is {self.salary}")

    @staticmethod
    def greet():
            print("good morning")

harry = Employee("harry",1500000,"javascript")
harry.name = "potter"
print(harry.name,harry.salary)
