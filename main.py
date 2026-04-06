from quiz import Quiz 

quizzes = [
    Quiz("시너지 ‘혁신가'에서 소환되는 기계는 단계별로 강화된다. \n다음 중 혁신가 7 시너지 효과로 등장하는 유닛은?", ["기계 곰", "T-Hex", "기계 드래곤", "기계 풍뎅이"], 3),
    Quiz("시즌 7에서 용 특성의 숨겨진 룰로 맞는 것은?", ["용 유닛은 2칸을 차지한다", "용 유닛은 아이템을 4개까지 장착 가능하다", "용 유닛은 시너지 효과를 받지 않는다", "동일한 드래곤은 2마리까지 배치 가능하다"], 1),
    Quiz("다음 중 아이템 조합 결과가 올바른 것은?", ["곡궁 + 곡궁 -> 거인의 결의", "BF 대검 + 곡궁 -> 거인 학살자", "쓸데없이 큰 지팡이 + 여신의 눈물 -> 쇼친의 창", "체인 조끼 + 망토 -> 정령의 형상"], 2),
    Quiz("시즌 4의 선택받은 자 시스템에서 맞는 설명은?", ["선택받은 자는 추가 시너지를 제공하지 않는다", "둘 이상의 선택받은 자를 얻을 수 있다", "선택받은 자는 상점에 동시에 2개가 등장할 수 있다", "선택받은 자는 항상 2성으로 등장한다"], 4),
    Quiz("비취 시너지의 특징으로 올바른 것은?", ["조각상은 그 자리에서 공격을 한다", "조각상 주변 유닛만 버프를 받는다", "조각상은 라운드마다 위치가 랜덤이다", "조각상은 파괴되지 않는다"], 2),
]

def show_menu():
    print("=================================")
    print("            롤토체스 퀴즈            ")
    print("=================================")
    print()
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print()
    print("=================================")


def get_user_input():
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


def main():
    while True:
        show_menu()

        choice = get_user_input()

        if choice is None:
            continue

        if choice == 1:
            q = Quiz(
                "정답은 1번 ",
                ["일", "이", "삼", "사"],
                1
            )

            q.show()

            answer = int(input("정답: "))

            if q.check_answer(answer):
                print("정답!")
            else:
                print("오답!")


        elif choice == 2:
            print("퀴즈 추가 기능 (아직 구현 안됨)")
        elif choice == 3:
            print("퀴즈 목록 기능 (아직 구현 안됨)")
        elif choice == 4:
            print("점수 확인 기능 (아직 구현 안됨)")
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break

        input("\n엔터를 누르면 메뉴로 돌아갑니다...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n프로그램이 안전하게 종료되었습니다.")
    except EOFError:
        print("\n입력이 종료되어 프로그램을 종료합니다.")