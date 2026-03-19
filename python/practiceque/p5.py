"""Word Frequency Counter

Write a Python program that asks the user to enter a sentence. Count how many times each word appears in the sentence and display the result"""
sen=input("Enter the sentence:")
for letter in sen :
  count=sen.count(letter)
  print(letter,":",count)
  