#SET (no duplicate, add(), update(), remove(), pop() , any data type,un ordered)  {}
my_set1 = {10, 20, 20, 30}
my_set2={10,20,50,60}
print(my_set1)  # {10, 20, 30}
#set removes the dupliate values \
new_set=my_set1.union(my_set2)
print(new_set)

new_set2=my_set1.intersection(my_set2)
print(new_set2)

new_set3= my_set1.difference(my_set2)
print(new_set3)

new_set4= my_set2.difference(my_set1)
print(new_set4)