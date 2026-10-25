class Employee:
    language = "python" # This is a class attribute
    salary = 1000000

    def getinfo(self):
        print(f"the langauge is {self.language}. the salary is {self.salary}")

harry = Employee()
harry.language = "c++"
harry.getinfo()
Employee.getinfo(harry)
# above both does identical tasks

