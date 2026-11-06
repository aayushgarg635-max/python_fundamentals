class Employe:
    company = "Google"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class coder:
     language = "Python"
     def showlanguages(self):
          print(f"from all languages here is your language:{self.language}")

class programmer(Employe,coder):
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
a.show()

