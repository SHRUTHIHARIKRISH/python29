"""Student Marks Management System

Write a Python program that stores student names and their marks in a dictionary. Allow the user to:

Add a new student and marks

Delete a student

Display all students and calculate the average marks"""

students={}
while(True):
  print("__STUDENTSLIST____")
  print("To add student enter 1")
  print("To delete student enter 2")
  print("To display student enter 3")
  print("To calaculate average enter 4")
  choice=int(input("ENTER A OPTION:"))
  if(choice == 1):
    name=(input("Enter the name:"))
    marks=int(input("Enter the marks:"))
    students[name]=marks
    print()
  elif(choice == 2):
    name=(input("Enter the name:"))
    if(name in students):
      del(students[name])
      print("Student deleted")
    else:
      print("student not found")
  elif(choice == 3):
    for name,marks in students.items():        #.items() returns both key and value
     print(name,":",marks)
  #to calculate the average marks of all students
  elif(choice == 4):
    total=0
    for marks in students.values():    #get all values such as marks
     total+=marks                       #0+mark of student
    average=total/len(students)        #tot marks of stud/tot stud
    print("Average marks:",average)
  else:
    print("EXIT")
    break



