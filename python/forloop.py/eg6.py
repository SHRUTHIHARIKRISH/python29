#get 10 nos ip and then find avg of the 10 nos using list

a=[]
for i in range (1,11):
  b=(int(input("enter the number")))
  a.append(b)
#print(a)
avg=sum(a)/10
print("avg=",avg)