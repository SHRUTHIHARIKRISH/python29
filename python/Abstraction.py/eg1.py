"""Abstraction we use:

ABC (Abstract Base Class)

@abstractmethod"""

from abc import ABC, abstractmethod
# Architect defines the
class FeaturePlan (ABC):   #You CANNOT create object of abstract class
  @abstractmethod
  def checkout(self):
    pass

  @abstractmethod
  def login(self):
    pass
# Developer implements it

class WebApp(FeaturePlan):

  def checkout(self):
    print("i am checkout")

  def login(self):
    print("login")

ob1=WebApp()
ob1.checkout()
ob1.login()