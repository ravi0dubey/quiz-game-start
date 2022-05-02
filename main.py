from data import question_data
from data1 import question_data1
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
your_score= 0

for key in question_data1:
    print(key)
    text = key["question"]
    answer= key["correct_answer"]
    new_question = Question(text,answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while(quiz.still_has_question() ):
    quiz.next_question()

print("\nYou've completed the quiz:")
print(f"Your Final score was {quiz.user_score}/{quiz.question_number}")

# below code in case we want to stop the quiz when user enters incorrect answer
    # if quiz.next_question():
    #     continue
    # else:
    #     break






















