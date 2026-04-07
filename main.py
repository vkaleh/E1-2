from quiz_game import QuizGame 

def main():
    game = QuizGame()   # 게임 객체 생성
    game.run()          # 게임 실행


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n프로그램이 안전하게 종료되었습니다.")
    except EOFError:
        print("\n입력이 종료되어 프로그램을 종료합니다.")