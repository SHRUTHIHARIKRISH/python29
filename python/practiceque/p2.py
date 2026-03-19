#check palindrome or not
text=(input("Enter number or text:"))
rev_text= text[::-1]   #string[start : end : step]
if(text == rev_text):
  print("It's palindrome")
else:
   ("It's not plaindrome")