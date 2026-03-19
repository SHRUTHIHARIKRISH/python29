"""how the function can be called from one file to another
use syntax like : "from file1 import add"
importing the function add from  the file1 to use in file2"""

# for multiplying many numbers
#using *args means can have many arguments in the function
#add function
def add(*args):
  tot=0
  for num in args:
    tot+=num
  return tot
print(add(1,2,3,4,5,6,7,8,9,10))


# "*kwargs"
#Keyword Arguments” (named arguments)
#👉 It collects values as a dictionary
def show(**kwargs):
  for key, value in kwargs.items():
    print(key, "=", value)

show(name="Shruthi", age=18, course="B.Tech")