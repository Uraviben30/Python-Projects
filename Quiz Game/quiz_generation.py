from question_model import Question  # Import the Question class
from data import question_data       # Import the list of question data (dictionary format)
from quiz_brain import QuizBrain     # Import the QuizBrain class to manage quiz logic

# Create an empty list to store Question objects
question_bank = []

# Loop through each question dictionary in question_data
for question in question_data:
    question_text = question["text"]        # Extract the question text
    question_answer = question["answer"]    # Extract the correct answer
    new_question = Question(question_text, question_answer)  # Create a Question object
    question_bank.append(new_question)      # Add the Question object to the list

# Create a QuizBrain object using the list of Question objects
quiz = QuizBrain(question_bank)

# Keep asking questions until there are no more left
while quiz.still_has_questions():
    quiz.next_question()

# Quiz is finished, print final result
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
