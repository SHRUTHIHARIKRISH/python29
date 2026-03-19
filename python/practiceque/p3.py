"""To-Do List Manager Write a Python program where the user can:

Add tasks to a list

Remove tasks from the list

Display all tasks

Exit the program"""
from os import remove
list=[]
while(True):
  print("____TASK MANAGER____")                          #condition under while loop coz its ruin loop
  a=print("To add task enter 1")
  a=print("To remove task enter 2")
  a=print("To display task enter 3")
  a=print("To exit enter 4")
  A=int(input("ENTER A OPTION"))
  if(A == 1):
      values=input("ADD TO DO LIST:")
      add=list.append(values)
      print()
  elif(A == 2):
      remove_values=input("DELETE THE TASK")
      delete=list.remove(remove_values)
      print()
  elif(A == 3):
      display=print(list)
      print()
  else:
      exit=print("EXIT")
      break


