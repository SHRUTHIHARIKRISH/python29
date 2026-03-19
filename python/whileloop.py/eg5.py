#find the sum of the num
num=int(input("Enter the number:"))
sum=0
while(num>0):
  sum+=num%10  # find the last digit
  num=num//10 #toremove the last digit
print(sum) #intendation is impt
