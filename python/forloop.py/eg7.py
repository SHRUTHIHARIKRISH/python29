#factorial of 5 12345

a=int(input("enter the number"))
fact=1
for i in range(1,a+1):
  #print(i)
  fact=fact*i
print(fact)