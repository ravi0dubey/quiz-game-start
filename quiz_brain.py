
class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list=q_list
        self.user_score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text}. (True/False)? :")
        self.verify_answer(user_answer, current_question.answer)
    #below code in case we want to stop the quiz when user enters incorrect answer
            #return self.verify_answer(user_answer,current_question.answer)


    def still_has_question(self):
        print(f"self.question_number: {self.question_number}")
        print(f"len(self.question_list) : {len(self.question_list)}")
        return self.question_number < len(self.question_list)

    def verify_answer(self,user_answer,answer):
        if user_answer == answer:
            self.user_score += 1
            print("you got it right!")
        else:
            print("That's wrong!")

        print(f"Correct answer was: {answer}")
        print(f"Your score is : {self.user_score}/{self.question_number}")
        print("\n")
        # below code in case we want to stop the quiz when user enters incorrect answer
        #return user_answer == answer



