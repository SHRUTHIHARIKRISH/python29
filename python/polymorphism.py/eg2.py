class emp():
  def __init__ (self,name,salary):
    self.peyar=name
    self.sal=salary

class manager(emp):
  def __init__(self,name,salary, department):
    super(). __init__(name ,salary)
    self.dept=department
  def display(self):
    print(self.peyar,self.sal,self.dept)

ob1=emp("SHRUTHI","1CR")
ob2=manager("SHRUTHI","1CR","DA")

ob2.display()