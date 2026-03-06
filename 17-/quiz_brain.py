class Quiz_brain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # question = self.question_list[self.question_number]
        #
        # if self.question_list[-1] != question:
        #     return True
        # else:
        #     return False
        # My answer does not include q12....

        #Angela's better way
        return self.question_number < len(self.question_list)


    def next_question(self):
        c_question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q.{self.question_number}: {c_question.text} (True/False): ")
        self.check_answer(u_answer, c_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}. ")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")




