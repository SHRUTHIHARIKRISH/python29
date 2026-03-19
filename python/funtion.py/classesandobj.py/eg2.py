class laptop():
  chargertype="C_TYPE"
  def _init_(self):
    self.brand=""
    self.price=34
  def setPrice(self, price):
    self.price-price
  def getPrice(self):
     print (self.price)
  
  @classmethod                               #used to change the class variable
  def changeChargerType (cls):
    cls.chargertype="B_TYPE"
    print("Charger type changed")
  @staticmethod                             #for simple function
  def info():
    print ("This is laptop class")

hp=laptop ()
hp.setPrice (20000)
hp.getPrice()
laptop.changeChargerType ()
hp.info()