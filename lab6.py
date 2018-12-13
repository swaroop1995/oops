class Employee:
    def assign(self):
        self.idno=101
        self.name="ravi"
    def display(self):
        print(self.idno)
        print(self.name)

e1=Employee()
#e1.dispaly()employye object has no attribute 'display'
e1.assign()
e1.display()
e2=Employee()
e2.assign()
e2.display()