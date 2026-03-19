count = 0

for i in range(1, 101):
    count += str(i).count('9')

print(count)


cout=0
for j in range(1,101):
  if(j % 3 == 0 and j % 5 == 0):
    cout += 1
print(cout)



#range(start, stop, step)
for i in range(1, 20, 2):
    print(i)