class a():
  def __init__(self):
    print ("A")
  def display (self):
    print ("you are in class a")

class b ():
    def __init__(self):
      super().__init__()   #super keyword calls the parent function first
      print ("B")          #then print B (nxt line)
def display (self):
       print ("you are in class b")

class c(b):
  def __init__(self):
    super().__init__()
    print ("C")
  def display (self):
     print ("you are in class C")


obl=b()
ob2=c()