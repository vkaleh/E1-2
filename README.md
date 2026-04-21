# Git과 함께하는 Python 첫 발자국 

## 1. 프로젝트 개요
Python 콘솔 환경에서 동작하는 퀴즈 게임을 구현하는 프로젝트로, 
JSON을 활용한 데이터 관리, 객체지향 설계, Git을 활용한 버전 관리를 경험한다.


## 2. 퀴즈 주제, 선정 이유
**롤토체스(TFT)**

개인적으로 관심 있는 게임을 주제로 선택하여 학습 동기를 높였다. <br>
모두 롤토체스 하세요^^7 
<br>

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
- 기록 확인
- 퀴즈 삭제
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
### 6-1. 데이터 스키마
| Key | Type | 설명 |
|:---:|:---:|:---:|
| **quizzes** | Array | 게임에 사용될 퀴즈 문제들의 리스트 |
| **best_score** | Integer | 사용자가 달성한 역대 최고 점수 |
| **history** | Array | 과거 게임 플레이 결과들의 로그 리스트 |
<br>

### 6-2. Quizzes 내부 구조 
| Key | Type | 설명 |
|:---:|:---:|:---:|
| **question** | String | 퀴즈 문제의 텍스트 내용 |
| **choices** | Array | 선택지 리스트 (4지선다 형식) |
| **answer** | Integer | 정답 인덱스 번호 |
| **hint** | String | 문제 풀이에 도움을 주는 힌트 텍스트 |
<br>

### 6-3. History 내부 구조
플레이가 종료될 때마다 아래 기록이 누적됨 
| Key | Type | 설명 |
|:---:|:---:|:---:|
| **timestamp** | String | 게임이 종료된 시각 (YYYY-MM-DD HH:MM:SS) |
| **num_problems** | Integer | 해당 회차에 출제된 총 문제 수 |
| **correct_count** | Integer | 사용자가 맞힌 정답 개수 |
| **score** | Integer | 백분율로 계산된 최종 점수 |
| **is_best** | Boolean | 해당 기록의 최고 점수 경신 여부 |
<br>

### 6-4. 데이터 파일의 역할
프로그램이 꺼져도 상태를 유지하게 해주고 <br>
로직과 데이터를 분리해서 유지보수성을 높임 
<br>

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

<br>

## 8. 결과

### 8-1. 프로그램 실행 결과 

#### 퀴즈 풀기 
<p>
<img width="363" height="944" alt="Screenshot 2026-04-09 at 2 53 50 PM" src="https://github.com/user-attachments/assets/8100cfd3-017d-4b44-8aa4-5065a1cdb092" />
</p>

<br>

#### 퀴즈 추가
<p>
<img width="268" height="454" alt="Screenshot 2026-04-09 at 2 55 15 PM" src="https://github.com/user-attachments/assets/3cc85920-27f5-4293-b060-1337cb8c0d4f" />
</p>

<br>


#### 퀴즈 목록 확인
<p>
<img width="421" height="451" alt="Screenshot 2026-04-09 at 2 52 05 PM" src="https://github.com/user-attachments/assets/fac98c7c-46da-44e9-8fd7-a9633fe02ae6" />
</p>

<br>


#### 기록 확인
<p>
<img width="262" height="355" alt="Screenshot 2026-04-09 at 2 58 23 PM" src="https://github.com/user-attachments/assets/5cd97e93-a75b-497d-9fde-8a93617b1e29" />
</p>

<p>
<img width="482" height="424" alt="Screenshot 2026-04-09 at 2 58 38 PM" src="https://github.com/user-attachments/assets/a4ceaf4e-8b50-499f-998d-519d3f67cb57" />
</p>

<br>

#### 퀴즈 삭제
<p>
<img width="419" height="449" alt="Screenshot 2026-04-09 at 3 04 06 PM" src="https://github.com/user-attachments/assets/8ceb0c11-e611-4d1c-9f5f-1322a9c6ed7f" />
</p>

<p>
<img width="415" height="462" alt="Screenshot 2026-04-09 at 3 04 22 PM" src="https://github.com/user-attachments/assets/f3a6ea1b-dbf4-49f8-8132-b6543169bdc5" />
</p>

<p>
<img width="421" height="436" alt="Screenshot 2026-04-09 at 3 04 31 PM" src="https://github.com/user-attachments/assets/7a3c3df6-e870-4c8b-bc35-66283e452128" />
</p>

<br>

#### 종료

<p>
<img width="244" height="211" alt="Screenshot 2026-04-09 at 3 11 21 PM" src="https://github.com/user-attachments/assets/d8df936f-d4eb-4007-8058-d2aa40aa174c" />
</p>
<br>

#### 사용자 입력 중단 처리 

<p>
<img width="665" height="260" alt="Screenshot 2026-04-09 at 3 05 14 PM" src="https://github.com/user-attachments/assets/424c927e-0588-437d-986c-4f9c96d87a01" />
</p>
<br>

### 8-2. 커밋 로그 
```bash
git log --oneline --graph
```

<p>
<img width="559" height="358" alt="Screenshot 2026-04-09 at 2 46 20 PM" src="https://github.com/user-attachments/assets/947eb6b3-dbba-487f-ab17-765c8cfe135d" />
</p>
<br>

### 8-3. Git 저장소 복제 실습 
#### git clone 
<p>
 <img width="560" height="114" alt="Screenshot 2026-04-14 at 10 53 16 AM" src="https://github.com/user-attachments/assets/01d97012-07d3-4cd6-ab05-e769fcad54b7" />
</p>
<br>

#### 복제된 저장소에서 변경
<p>
<img width="564" height="98" alt="Screenshot 2026-04-14 at 11 01 36 AM" src="https://github.com/user-attachments/assets/9c2a6211-c0e9-4388-a77d-f5acaef66492" />
</p>
<p>
<img width="486" height="140" alt="Screenshot 2026-04-14 at 11 19 30 AM" src="https://github.com/user-attachments/assets/6a2a2c1d-0ab5-4525-9b23-36b8199e8892" />
</p>
<br>

### 작업하던 로컬 디렉토리에서 pull로 변경사항 가져옴 
<p>
<img width="561" height="294" alt="Screenshot 2026-04-14 at 11 21 30 AM" src="https://github.com/user-attachments/assets/23c84a24-4c8b-495a-ac95-647b6df74d48" />
</p>
<br>

## 9. 보충 설명 

### - [git push] VS [git push origin main]
- **git push** <br>
  미리 연결된 곳으로 푸시. 맨 처음에 git push -u origin main을 해두었다면
  그 다음부터는 git push만 해도 origin main으로 감 
- **git push origin main** <br>
  origin 이라는 서버의 main 브랜치로 보냄. 어느 브랜치에 있든 상관없이 명확하게 타겟을 지정하므로 실수 방지
<p align="center">&nbsp;</p>

### - 클래스의 역할과 책임 
역할 : 클래스명 (예: 학생) <br>
책임 : 클래스의 기능 <br>
역할 안에 여러 책임이 있다고 볼 수 있음 <br>

클래스 없이 함수만으로 기능 구현은 가능하겠지만, 관련 데이터를 묶어줄 객체가 없게 됨 <br>
그래서 매개변수로 값을 매번 넘겨줘야 함
<p align="center">&nbsp;</p>

### - @staticmethod 와 @classmethod 
| 특징 | staticmethod | classmethod | 
|:---:|:---:|:---:|
| **첫 번째 인자** | 없음 | cls |
| **클래스 변수 접근** | 불가능 | 가능 |
| **주 사용 목적** | 유틸리티/헬퍼 기능 | 대안 생성자/클래스 변수 수정 |
| **상속 시 동작** | 클래스 정보가 없어서, 어디서 호출해도 동일한 동작 | cls가 자식 클래스로 자동 변경되어 동작 |

둘다 클래스명.함수명()으로 바로 호출해서 사용한다는 점은 같음 <br>

staticmethod는 주로 클래스와 관련있지만, 객체 생성할 필요가 없을 때 주로 기능 관련으로 많이 사용함 <br>
일반 클래스 함수에는 첫번째 매개변수로 self를 적지만, staticmethod에서는 적지 않음 <br>
<p align="center">&nbsp;</p>

### - JSON 특징
- 데이터 크기가 커질수록 성능저하가 일어나는 이유 : 파일 전체를 처음부터 다 읽고, 중간에 멈출 수 없음
또, 파싱된 데이터 전체를 메모리에 올려야 함 <br>
<p align="center">&nbsp;</p>

### - JSON 파일 손상을 막기 위한 방법
- JSON Lines
```bash
# 스트리밍 방식 — 한 줄씩 읽기
import jsonlines

with open("data.jsonl") as f:
    for line in f:
        item = json.loads(line)   # 한 줄씩 파싱
        process(item)             # 처리 후 메모리 해제
        # 전체를 메모리에 올리지 않음 
```
<br>

- Atomic Write
```bash
import os
import json

def save_state_safe(data):
    # 1단계: 임시 파일에 완전히 씀
    with open("state.tmp", "w") as f:
        json.dump(data, f)
    
    # 2단계: 완성됐으면 그때 교체
    os.replace("state.tmp", "state.json")
```
