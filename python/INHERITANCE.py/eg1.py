# Inheritance means one class can use properties of another class

class dad():
  def money (self):
    print ("dad money")
class land():
  def important (self):
    print ("important land")
class son1 (dad, land):
    pass
class son2 (dad) :
   pass
class son3 (dad):
   pass
s2=son2 ()
s2.money()
#inheritance can over write(override) which is  intial class can be changed



#multiple inheritance
class A:
    pass

class B:
    pass

class C(A, B):
    pass

#Multilevel Inheritance
class A:
    pass

class B(A):
    pass

class C(B):
    pass


#Hierarchical Inheritance
class A:
    pass

class B(A):
    pass

class C(A):
    pass
