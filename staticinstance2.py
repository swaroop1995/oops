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
        print(self.comp_name)
        print(self.comp_cno)

e1=Employee()
e1.assign()
e1.display()
print("------------")
e2=Employee()
e2.assign(101,"ravi")
e2.display()