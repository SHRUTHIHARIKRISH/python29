#reverse the num or string
num=int(input("Enter the number:"))
rev=0
while(num>0):
  digit=num%10 #to find the last digit
  rev=rev*10+digit #to return the last digit
  num=num//10 # to remove the last digit and update num
print(rev)
