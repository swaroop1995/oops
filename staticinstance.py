class Employee:
    comp_name="sathya"
    comp_cn0=905249
    @staticmethod
    def displayInfo():
        print(Employee.comp_name)
        print(Employee.comp_cno)

    def assign(self,idno=0,name=None):
        self.idno=idno
        self.name=name

    def display(self):
        print(self.idno)
        print(self.name)

e1=Employee()
e1.assign(101,"ravi")
e1.display()
print("-------------")
e2=Employee()
e2.assign(102,"kumar")
e2.display()
