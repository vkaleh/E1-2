# Git과 함께하는 Python 첫 발자국 

## 1. 프로젝트 개요

## 2. 퀴즈 주제, 선정 이유

## 3. 실행 방법

## 4. 기능 목록

## 5. 파일 구조

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
