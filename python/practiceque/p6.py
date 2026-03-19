"""Fibonacci Series Generator

Write a Python program that asks the user for a number n and prints the first n numbers of the Fibonacci sequence."""
a=0
b=1
n=int(input("Enter the number of fibonacci"))
for i in range(n):
  print(a)
  c=a+b
  a=b
  b=c