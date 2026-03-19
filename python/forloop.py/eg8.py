#check its prime num also find the prime numbers from 1 to 100
num=int(input("Enter the number:"))
count=0
for i in range(1,num+1):
  if(num%i==0):
    count=count+1
if(count==2):
  print("Its prime")

else:
  print("Its not prime")


for p in range(1, 101):
    cout = 0
    for i in range(1, p+1):
        if p % i == 0:
            cout = cout + 1
    if cout == 2:
       print("The prime numbers from 1 to 100 is:",p)