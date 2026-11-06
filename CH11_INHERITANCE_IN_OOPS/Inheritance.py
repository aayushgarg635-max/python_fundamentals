class Employe:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class programmer:
#     company = "Google research"
#     def show(self):
#         print(f"the name is {self.name} is and salary is {self.salary}")

#     def showlanguage(self):
#         print(f"the language is {self.langauge}")    

# INHERITED CLASS 
class programmer(Employe):
      company = "Google Research"
      def showlanguage(self):
           print(f"tThe name is {self.name} and he is good with language{self.language}")


a = Employe()
a.name = "Rahul"
a.salary = "85000"
b = programmer()

print(a.company)
print(a.name)
print(a.salary)

print(b.company)



