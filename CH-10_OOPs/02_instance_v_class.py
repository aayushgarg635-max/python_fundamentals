class Employee:
    language = "python" # This is a class attribute
    salary = 1000000

harry = Employee()
harry.language = "Javascript" # this is an instance attribute 
print(harry.language)
print(harry.salary)

# instance attributes take prefrence over class attributes during assignments and retrieval

