# Git과 함께하는 Python 첫 발자국 

## 1. 프로젝트 개요

## 2. 퀴즈 주제, 선정 이유

## 3. 실행 방법

## 4. 기능 목록

## 5. 파일 구조

## 6. 데이터 파일 설명

## 7. 구현 방법 

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

#### - 변경사항 커밋 및 푸시
```bash
% git add .
% git commit -m "feat: Quiz 클래스 구현" -m "- Quiz.py 생성
dquote> - main.py에 퀴즈 출력 테스트 코드 추가"
% git push
```
