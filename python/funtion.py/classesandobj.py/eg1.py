class laptop:
  price=0
  processor=0
  ram=0

hp=laptop()  #assigning the object to the class
dell=laptop()
lenovo=laptop()

hp.price="$4500"  #assigning the values in the varible of object in the class
dell.price="$5600"
lenovo.price="$8900"

hp.processor="i3"
dell.processor="i5"
lenovo.processor="i7"

hp.ram="2g"
dell.ram="4g"
lenovo.ram="6g"

print(lenovo.price)
print(lenovo.processor)
print(lenovo.ram)