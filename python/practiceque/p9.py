"""Quiz Game

Write a Python program that stores 5–10 questions and answers in a dictionary. Ask each question to the user and check if the answer is correct. At the end, display the total score."""
quiz = {
    "What is the capital of India?": "delhi",
    "What is 2 + 2?": "4",
    "Which language is used for AI?": "python",
    "What color is the sky?": "blue",
    "How many days in a week?": "7"
}
score=0
for question , answer in quiz.items():
  user_ans=input(question + "")
  if(user_ans.lower() == answer):
    score+=1
    print("Correct answer!")
  else:
    print("Incorrect answer!")
print("Your score is:",score)