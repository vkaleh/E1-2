class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices  # 리스트
        self.answer = answer    # 정답 번호 (1~4)

    def show(self):
        print(f"\n{self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def check_answer(self, user_input):
        return user_input == self.answer