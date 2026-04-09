# 퀴즈 게임 전체를 관리하는 클래스

import json
import random
import os
from quiz import Quiz 

class QuizGame:

    # 파일 경로 설정
    DB_FILE = "state.json"

    # 기본 퀴즈 데이터 (state.json이 없을 때 사용)
    DEFAULT_QUIZZES = [
        Quiz("시너지 ‘혁신가'에서 소환되는 기계는 단계별로 강화된다. \n다음 중 혁신가 7 시너지 효과로 등장하는 유닛은?", ["기계 곰", "T-Hex", "기계 드래곤", "기계 풍뎅이"], 3, "혁신가 시너지의 최종 단계로, 가장 거대하고 강력한 존재감을 뽐내는 생명체."),
        Quiz("시즌 7에서 용 특성의 숨겨진 룰로 맞는 것은?", ["용 유닛은 2칸을 차지한다", "용 유닛은 아이템을 4개까지 장착 가능하다", "용 유닛은 시너지 효과를 받지 않는다", "동일한 드래곤은 2마리까지 배치 가능하다"], 1, "용은 크기가 큽니다."),
        Quiz("다음 중 아이템 조합 결과가 올바른 것은?", ["곡궁 + 곡궁 -> 거인의 결의", "BF 대검 + 곡궁 -> 거인 학살자", "쓸데없이 큰 지팡이 + 여신의 눈물 -> 쇼친의 창", "체인 조끼 + 망토 -> 정령의 형상"], 2, "힌트가 없습니다."),
        Quiz("시즌 4의 선택받은 자 시스템에서 맞는 설명은?", ["선택받은 자는 추가 시너지를 제공하지 않는다", "둘 이상의 선택받은 자를 얻을 수 있다", "선택받은 자는 상점에 동시에 2개가 등장할 수 있다", "선택받은 자는 항상 2성으로 등장한다"], 4, "선받자는 상점에서 구매하자마자 즉시 필드에 투입하는 용도로 많이 쓰입니다."),
        Quiz("비취 시너지의 특징으로 올바른 것은?", ["조각상은 그 자리에서 공격을 한다", "조각상 주변 유닛만 버프를 받는다", "조각상은 라운드마다 위치가 랜덤이다", "조각상은 파괴되지 않는다"], 2, "비취 시너지의 특징과 비슷합니다."),
    ]


    def __init__(self):         # 초기화 
        self.quizzes, self.best_score = self.load_quizzes()
    

    # ==================== 파일 관리 ====================
    # 파일 불러오기 (state.json에서 퀴즈와 최고점수를 로드)
    def load_quizzes(self):
        # 파일이 없는 경우
        if not os.path.exists(self.DB_FILE):
            print("[안내] 저장된 데이터가 없어 기본 퀴즈를 사용합니다.")
            return list(self.DEFAULT_QUIZZES), 0
        
        # 파일이 있는 경우 읽기 
        try:
            with open(self.DB_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.quizzes = [Quiz.from_dict(d) for d in data["quizzes"]]
            self.best_score = data.get("best_score", 0)  # 최고점수 없으면 0

            print(f"[안내] {len(self.quizzes)}개의 퀴즈를 불러왔습니다.")
            return self.quizzes, self.best_score
        
        # 3. 파일이 손상되었거나 형식이 잘못된 경우 처리
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"[경고] 데이터 파일이 손상되어 기본 퀴즈를 사용합니다. ({e})")
            return list(self.DEFAULT_QUIZZES), 0
        
        except Exception as e:
            print(f"\n[오류] 예상치 못한 오류 발생: {e}")
            return list(self.DEFAULT_QUIZZES), 0
    

    # 현재 quizzes 리스트와 최고점수를를 state.json에 저장
    def save_quizzes(self):
        try:
            data = {
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score, 
            }
            with open(self.DB_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("[안내] 데이터가 저장되었습니다.")
        except Exception as e:
            print(f"데이터 저장 중 오류 발생: {e}")
    

    # ====================게임 실행====================
    def show_menu(self):
        print("=================================")
        print("            롤토체스 퀴즈            ")
        print("=================================")
        print()
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 종료")
        print()
        print("=================================")


    # 게임 메인 루프 
    def run(self):
        while True:
            self.show_menu()

            choice = self.get_menu_input()

            if choice is None:
                continue

            if choice == 1:
                self.play_quiz()

            elif choice == 2:
                self.add_quiz()

            elif choice == 3:
                self.view_quizzes()

            elif choice == 4:
                self.view_score()

            elif choice == 5:
                self.delete_quiz()    

            elif choice == 6:
                print("프로그램을 종료합니다.")
                break

            input("\n엔터를 누르면 메뉴로 돌아갑니다...")
    

    # ====================입력 관련==================== 
    def get_menu_input(self):
        try:
            user_input = input("선택: ").strip()            # 앞뒤 공백 제거

            # 빈 입력 처리
            if user_input == "":
                print("입력이 비어있습니다. 다시 입력해주세요.\n")
                return None

            # 숫자 변환 시도
            choice = int(user_input)

            # 범위 체크
            if choice < 1 or choice > 5:
                print("1~5 사이의 숫자를 입력해주세요.\n")
                return None
            return choice

        except ValueError:
            print("숫자를 입력해주세요.\n")
            return None
        

    def get_number_input(self, prompt, min_value, max_value, allow_hint = False):
        while True:
            user_input = input(prompt).strip()

            if user_input == "":
                print("입력이 비어있습니다.")
                continue

            try:
                value = int(user_input)

                # 힌트 기능이 활성화되고 0을 입력한 경우
                if allow_hint and value == 0:
                    return 0  # 0을 반환하면 play_quiz에서 처리

                if value < min_value or value > max_value:
                    print(f"{min_value}~{max_value} 사이 숫자를 입력하세요.")
                    continue
                return value

            except ValueError:
                print("숫자를 입력하세요.")


    def get_text_input(self, prompt):
        while True:
            text = input(prompt).strip()
            if text == "":
                print("입력이 비어있습니다.")
                continue
            return text


    # ====================퀴즈 관련==================== 
    # 퀴즈를 풀고 점수를 계산
    def play_quiz(self):
        # 퀴즈가 없는 경우 처리
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        
        # 풀 문제 수를 사용자로부터 입력받기
        num_problems = self.get_number_input(
            f"\n풀 문제 수를 입력하세요 (1~{len(self.quizzes)}): ",
            min_value=1,
            max_value=len(self.quizzes)
        )

        print(f"\n퀴즈를 시작합니다! (총 {num_problems}문제)\n")

        # 문제 순서를 랜덤하게 섞기
        shuffled_quizzes = self.quizzes.copy()
        random.shuffle(shuffled_quizzes)

        # 선택한 문제 수만큼만 추출
        selected_quizzes = shuffled_quizzes[:num_problems]

        score = 0.0
        hint_used = False  # 힌트 사용 여부 추적

        for idx, quiz in enumerate(selected_quizzes, 1):
            print("---------------------------------")
            print(f"[문제 {idx}]")

            quiz.show()

            # 입력 처리 
            answer = self.get_number_input(
                "정답 입력 (1~4) (힌트는 0): ", 1, 4, allow_hint = True)
            
            # 힌트 요청 처리
            if answer == 0:
                hint_used = True
                print(f"\n힌트: {quiz.hint}") 

                # 다시 입력받기
                answer = self.get_number_input("정답 입력 (1~4): ", 1, 4)

            points_earned = 0
            # 정답 체크
            if quiz.check_answer(answer):
                
                if hint_used:
                    points_earned = 0.5 # 힌트 사용 시 0.5 획득
                    hint_used = False   # 초기화
                else:
                    points_earned = 1.0 # 힌트 미사용 시 1 획득
                
                print("\nO 정답입니다!")
                score += points_earned        
            else:
                print(f"\nX 오답입니다! (정답: {quiz.answer})")
            print(f"(+{int(points_earned / num_problems * 100)}점 | 현재 점수: {int(score / num_problems * 100)}점)")

        # 점수 계산
        percentage = int(score / num_problems * 100)

        # 결과 출력
        print("=================================")
        print(f"결과: {num_problems}문제 중 {score}문제 정답!")
        print(f"점수: {percentage}점")

        # 최고점수 갱신
        if percentage > self.best_score:
            self.best_score = percentage
            print(f"!!!!!!! 새로운 최고 점수입니다 !!!!!!! ({self.best_score}점)")
            self.save_quizzes()  # 파일에 저장
        print("=================================")
        return
    

    def add_quiz(self):
        print("---------------------------------")
        print("새로운 퀴즈를 추가합니다.\n")

        question = self.get_text_input("문제를 입력하세요: ")

        choices = []
        for i in range(4):
            choice_text = self.get_text_input(f"선택지 {i+1}: ")
            choices.append(choice_text)

        answer = self.get_number_input("정답 번호 (1~4): ", 1, 4)

        # 힌트 입력하기
        hint = self.get_text_input("힌트를 입력하세요: ")
        if not hint:
            hint = "힌트가 없습니다."

        new_quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(new_quiz)

        self.save_quizzes()
        print("\n퀴즈가 추가되었습니다!")
    

    def view_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.\n")
            return
        
        print("\n---------저장된 퀴즈 목록---------")
        print(f"총 {len(self.quizzes)}개\n")
        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"[{idx}] {quiz.question}\n")
        print("---------------------------------")
    

    def view_score(self):
        print("\n------------최고 점수------------")
        if self.best_score == 0:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")
        print("---------------------------------")

    def delete_quiz(self):
        # 퀴즈가 없는 경우 처리
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.\n")
            return
        
        print("---------------------------------")
        print("삭제할 퀴즈를 선택하세요.\n")
        
        # 등록된 모든 퀴즈 표시
        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"[{idx}] {quiz.question}")
        
        # 삭제할 퀴즈 번호 입력받기
        delete_num = self.get_number_input(
            f"\n삭제할 퀴즈 번호 (1~{len(self.quizzes)}): ",
            min_value=1,
            max_value=len(self.quizzes)
        )
        
        # 확인 메시지
        deleted_quiz = self.quizzes[delete_num - 1]
        confirm = input(f"\n'{deleted_quiz.question}'을(를) 삭제하시겠습니까? (y/n): ")
        
        if confirm.lower() == 'y':
            self.quizzes.pop(delete_num - 1)  # 해당 인덱스의 퀴즈 삭제
            self.save_quizzes()  # 파일에 저장
            print("\n퀴즈가 삭제되었습니다!")
        else:
            print("\n삭제가 취소되었습니다.")
        print("---------------------------------")