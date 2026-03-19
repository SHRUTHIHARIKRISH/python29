print("WIN" == "WIN")#INTENDATION IS IMPT
print("WIN" == "WINN")


num=int(input("enter the number less than 20d"))
if(num % 2 == 0):
    print("EVEN")

#MINI CALCULATOR
x=int(input(("1 for ADD\n2 for SUBTRACT\n3 for MULTIPLY\n4 for DIVIDE\n")))
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
if(x == 1):
  print(a+b)
elif (x == 1):
  print(a-b)
elif (x== 1):
  print(a*b)
elif (x == 1):
  print(a/b)
else:
  print("INVALID")