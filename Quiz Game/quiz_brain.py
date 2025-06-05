class QuizBrain:

    def __init__(self,q_list):
        # Initialize with a list of questions
        self.question_number=0  # Keeps track of the current question index
        self.score=0            # Keeps track of the user's score
        self.question_list=q_list  # Stores the list of question objects

    def still_has_questions(self):
        # Returns True if there are more questions left to ask
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Retrieves the current question and asks the user for input
        current_question=self.question_list[self.question_number]
        self.question_number +=1  # Move to the next question
        user_answer=input(f"Q.{self.question_number}:{current_question.text}(True/False)")
        self.check_answer(user_answer,current_question.answer)  # Check the user's answer

    def check_answer(self,user_answer,correct_answer):
        # Compares user answer with the correct answer
        if user_answer.lower() == correct_answer.lower():
            self.score +=1  # Increase score if correct
            print("Correct!")
        else:
            print("Incorrect!")
        # Show the correct answer and current score
        print(f"The correct answer was {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}.")
        print("\n")
