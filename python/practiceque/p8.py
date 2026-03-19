"""Mini Banking System

Write a Python program to manage bank accounts using a dictionary. Each account has a unique account number and balance. The program should allow the user to:

Deposit money

Withdraw money

Check balance

Exit the program"""
bank={101:5000,102:3900,103:4500}
while(True):
  print("1.Money Deposite")
  print("2.Money Withdraw")
  print("3.Check Balance")
  print("4.Exit")
  choice=int(input("Enter the choice:"))
  if(choice == 1):
    acc=int(input("Enter the acc number:"))

    if(acc in bank):
       mon=int(input("Enter the money:"))
       bank[acc]+=mon   # the dictionary should use[] to access an element
       print("Money deposited")
    else:
      print("Account not found")
  elif(choice == 2):
    acc=int(input("Enter the acc number:"))

    if(acc in bank):
      mon=int(input("Enter the money:"))
      if bank[acc]>mon :
        bank[acc]-=mon
        print("Money withdraw")
      else:print("Insufficient balance")
    else:
      print("Account not found")
  elif(choice == 3):
    acc=int(input("Enter the acc number:"))
    if(acc in bank):
      print(acc,":",bank[acc])
    else:
      print("Account not found")
  elif(choice == 4):
     print("Exit")


