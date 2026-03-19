class animal():
  def sound(self):
    print("Animal makes sound")

class dog(animal):
  def sound(self):
    print("Dog barks")

class bird(animal):
  def sound(self):
    print("Birds sing")

a1=animal()
a2=dog()
a3=bird()

a1.sound()
a2.sound()
a3.sound()



class person():
  def __init__(self,name):
    self.peyar =name

class student(person):
  def __init__(self,name,grade):
    super().__init__(name)
    self.grade=grade
  def display(self):
    print(self.peyar,self.grade)


s2=student("SHRUTHI","A")


s2.display()



class shape():
  def area(self):
    return 0

class rectangle(shape):
   def area(self):
    l=10
    b=20
    print("area of a rectangle is :",l*b)

s1=rectangle()
s1.area()

