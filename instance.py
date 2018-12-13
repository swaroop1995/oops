class Employee:
    def display(self):
        print(self.idno)
        print(self.name)
    def assign(self,id,na):
        self.idno=id
        self.name=na
e1=Employee()
e1.assign(101,"ravi kumar")
e1.display()

