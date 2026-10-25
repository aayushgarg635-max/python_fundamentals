class Employee:
    language = "python" # This is a class attribute
    salary = 1000000

harry = Employee()
harry.name = "harry" # This is an instance atrribute
print(harry.salary,harry.language)

aayush = Employee()
print(aayush.salary)

rohan = Employee()
rohan.name = "rohan kumar"
print("rohan.language")


# here name is object attributes and salary and langauge are class attributes as they belongs to class

