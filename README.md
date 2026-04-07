# Git과 함께하는 Python 첫 발자국 

## 1. 프로젝트 개요
Python 콘솔 환경에서 동작하는 퀴즈 게임을 구현하는 프로젝트로, 
JSON을 활용한 데이터 관리, 객체지향 설계, Git을 활용한 버전 관리를 경험한다.


## 2. 퀴즈 주제, 선정 이유
**롤토체스(TFT)**

개인적으로 관심 있는 게임을 주제로 선택하여 학습 동기를 높였다.

## 3. 실행 방법
Python version : 3.12.13

```bash
% git clone ....git
% cd E1-2
% python main.py
```

## 4. 기능 목록
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 확인
- 점수 확인
- 종료하기 

## 5. 파일 구조

```bash
E1-2
├── main.py              # 메인 파일
├── quiz_game.py         # QuizGame 클래스
├── quiz.py              # Quiz 클래스
├── state.json           # 퀴즈 데이터 및 점수
└── README.md
```

## 6. 데이터 파일 설명

## 7. 구현 순서

### 7-1. Git 저장소 설정
```bash 
username@c4r2s8 ~ % mkdir e1-2
username@c4r2s8 ~ % cd e1-2
username@c4r2s8 e1-2 % git init
Initialized empty Git repository in /Users/username/e1-2/.git/
username@c4r2s8 e1-2 % git config user.name ...
username@c4r2s8 e1-2 % git config user.email ...
username@c4r2s8 e1-2 % git init
Reinitialized existing Git repository in /Users/username/e1-2/.git/
username@c4r2s8 e1-2 % touch README.md .gitignore
username@c4r2s8 e1-2 % nano .gitignore
username@c4r2s8 e1-2 % git add .
username@c4r2s8 e1-2 % git commit -m "Initial commit"
[main (root-commit) fea9fc2] Initial commit
 2 files changed, 216 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
username@c4r2s8 e1-2 % git remote add origin https://github.com/.../E1-2.git
username@c4r2s8 e1-2 % git branch -M main
username@c4r2s8 e1-2 % git push -u origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 6 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 2.08 KiB | 2.08 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/.../E1-2.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

<br>

### 7-2. 메뉴 기능 만들기

#### - 입력 예외 처리 추가

#### - 변경사항 커밋 및 푸시
```bash
% git pull 
% git add .
% git commit -m "feat: Quiz 클래스 구현" -m "- Quiz.py 생성
dquote> - main.py에 퀴즈 출력 테스트 코드 추가"
% git push
```

<br>

### 7-3. Quiz 클래스 생성

#### - 기본 퀴즈 데이터 작성

<br>

### 7-4. 퀴즈 풀기 기능 추가

#### - 브랜치 추가 및 병합 
```bash
% git checkout -b feature/play-quiz
git add .
git commit -m "Feat: 퀴즈 풀기 기능 구현"

git checkout main
git merge feature/play-quiz
git push
```
<p>
<img width="613" height="142" alt="Screenshot 2026-04-06 at 1 19 30 PM" src="https://github.com/user-attachments/assets/cb8c59a6-dc70-4bd3-a397-2733d41ed088" />
</p><br>

### 7-5. 퀴즈 추가 기능 추가

#### - JSON 파일이 손상되었을 때 메시지 출력, 기본 퀴즈 데이터로 초기화 
<p>
<img width="936" height="429" alt="Screenshot 2026-04-06 at 3 05 33 PM" src="https://github.com/user-attachments/assets/5fa5dd82-cc4e-4f0a-a7b8-c85d145c4587" />
</p><br>

### 7-6. 퀴즈 목록 확인 기능 추가

### 7-7. 점수 확인 기능 추가

### 7-8. QuizGame 클래스로 리팩토링

변경 전 : 함수 기반 구조 
```bash
def load_quizzes():
    pass

def save_quizzes():
    pass

def play_quiz():
    pass
```

<br>

변경 후 : 클래스 기반 구조
```bash
class QuizGame:
    def __init__(self):
        pass
    
    def load_quizzes(self):
        pass
    
    def save_quizzes(self):
        pass
    
    def play_quiz(self):
        pass
    
    def run(self):
        pass
```

**주요 개선사항**<br>
객체지향 설계: 전역변수를 클래스 변수로 변경<br>
캡슐화: 게임 로직을 run() 메서드로 통합<br>
자동화: 데이터 로드/저장을 __init__과 save_quizzes()로 자동화<br>
재사용성: 게임 객체를 다른 곳에서도 재사용 가능<br>

## 8. 보충 설명 

### - [git push] VS [git push origin main]
- **git push** <br>
  미리 연결된 곳으로 푸시. 맨 처음에 git push -u origin main을 해두었다면
  그 다음부터는 git push만 해도 origin main으로 감 
- **git push origin main** <br>
  origin 이라는 서버의 main 브랜치로 보냄. 어느 브랜치에 있든 상관없이 명확하게 타겟을 지정하므로 실수 방지 
