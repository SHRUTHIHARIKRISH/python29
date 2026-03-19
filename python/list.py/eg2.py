#Sum of all numbers in a list
a=[1,2,3,4]
sum=0
for item in a :
  sum=sum+item%10
  item=item // 10
print(sum)