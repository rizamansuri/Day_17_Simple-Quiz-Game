from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Creating Question bank which consist of question and correct answer
question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

# Initializing the quiz with question bank list
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

# Showing quit completion message
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
