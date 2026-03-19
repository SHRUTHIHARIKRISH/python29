a=0
b=1
for i in range (10):
  print(a)
  c=a+b
  a=b
  b=c


for j in range(1,6):
  print("*"*j)



for n in range(1,6):
   print("the cube of",n,"is:",n*n*n)


for x in range(1,6):
  print() #gives space btw lines
  for y in range(1,x+1):
   print(y,end="")#print the on iteration nxt line