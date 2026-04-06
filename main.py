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
            print("퀴즈 풀기 기능 (아직 구현 안됨)")
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