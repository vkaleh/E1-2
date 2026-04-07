class Quiz:
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices  # 리스트
        self.answer = answer    # 정답 번호 (1~4)
        self.hint = hint

    def show(self):
        print(f"\n{self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def check_answer(self, user_input):
        return user_input == self.answer
    
    # 객체 상태를 딕셔너리로 변환 (JSON 저장용)
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }
    
    # 딕셔너리 데이터를 기반으로 객체 생성 (JSON 불러오기용)
    @classmethod
    def from_dict(cls, data):
        return cls(data["question"], data["choices"], data["answer"])