class Employee:
    comp_name="sathya"
    comp_cno=905249
    @staticmethod
    def displayInfo():
        print(Employee.comp_name)
        print(Employee.comp_cno)

    def assign(self,id=0,na=None):
        self.idno=id
        self.name=na

    def display(self):
        print(self.idno)
        print(self.name)

print(type(Employee))
e1=Employee()
e1.assign()
e1.display()
Employee.displayInfo()
print("----------------")
e2=Employee()
print(e2.comp_name)
print(e2.comp_cno)
e2.assign(10,"kumar")
e2.display()
print(type(e2))
print("---------------")
e3=Employee()
e3.displayInfo()
e3.assign(103,"kumar")
e3.display()
print("------0--------")
