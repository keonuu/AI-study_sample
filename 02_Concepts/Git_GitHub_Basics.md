# Git/GitHub 입문

Tags: `Git`, `GitHub`, `Repository`, `Commit`, `Staging`, `Beginner`

## Summary

Git은 파일 변경 이력을 저장하는 도구이고, GitHub는 Git repository를 온라인에 보관하고 공유하는 서비스다. Git은 내 컴퓨터에서 동작하고, GitHub는 온라인 서비스다. `git add`는 다음 commit에 넣을 파일을 고르는 단계이고, `git commit`은 고른 변경사항을 실제 저장 지점으로 기록하는 단계다.

## Why Git Matters

Git을 쓰면 프로젝트의 변경 이력을 남길 수 있다.

예를 들어 30일 AI 학습 프로젝트에서는 다음과 같은 저장 지점을 만들 수 있다.

```text
commit 1: 30일 학습 플랜 생성
commit 2: Day 4 Git 학습 노트 작성
commit 3: Python 예제 코드 추가
commit 4: RNA-seq pipeline 개념 노트 작성
```

이렇게 기록하면 나중에 언제 어떤 파일을 왜 바꿨는지 추적할 수 있다.

## Git vs GitHub

Git:

```text
내 컴퓨터에서 파일 변경 이력을 관리하는 도구
```

GitHub:

```text
Git repository를 온라인에 보관하고 공유하는 서비스
```

비유:

```text
Git = 내 노트북 안의 연구노트 변경 기록
GitHub = 그 연구노트를 온라인에 백업하고 공유하는 곳
```

## Core Concepts

Repository:

```text
Git이 변경 이력을 관리하는 프로젝트 폴더
```

Commit:

```text
변경사항을 하나의 저장 지점으로 기록하는 것
```

Staging Area:

```text
다음 commit에 넣을 파일을 임시로 올려두는 공간
```

Branch:

```text
작업 흐름을 나눠서 실험하는 가지
```

Push:

```text
내 컴퓨터의 commit을 GitHub 같은 원격 저장소에 업로드하는 것
```

Pull:

```text
GitHub 같은 원격 저장소의 변경사항을 내 컴퓨터로 가져오는 것
```

## Basic Workflow

```text
파일 수정
→ git status로 변경 확인
→ git add로 commit할 파일 선택
→ git commit으로 저장 지점 생성
```

명령어:

```powershell
git status --short
git add .
git commit -m "docs: initialize AI 30-day learning plan"
```

## Commands Practiced

현재 폴더를 Git repository로 만든다.

```powershell
git init
```

현재 상태를 확인한다.

```powershell
git status --short
```

현재 폴더의 모든 변경사항을 staging area에 올린다.

```powershell
git add .
```

staging area에 올라간 변경사항을 commit으로 기록한다.

```powershell
git commit -m "docs: initialize AI 30-day learning plan"
```

가장 최근 commit을 확인한다.

```powershell
git log --oneline -1
```

## Actual Practice Result

학습 프로젝트 폴더:

```text
F:\MyDesktop\AI_30Day_MasterPlan
```

첫 commit:

```text
ce8e398 docs: initialize AI 30-day learning plan
```

결과:

```text
37 files changed
1782 insertions
```

## Important Distinctions

`git add`:

```text
이번 commit에 넣을 파일을 고르는 단계
```

`git commit`:

```text
고른 변경사항을 실제 저장 지점으로 기록하는 단계
```

`git status --short`에서 `??`:

```text
아직 Git이 추적하지 않는 새 파일
```

`git status --short`에서 `A`:

```text
새 파일이 staging area에 올라간 상태
```

아무 출력 없음:

```text
commit되지 않은 변경사항이 없는 깨끗한 상태
```

## What Is .gitignore?

`.gitignore`는 Git에게 "이 파일이나 폴더는 기록하지 말라"고 알려주는 설정 파일이다.

예를 들어 Python 프로젝트에서는 다음을 Git에 넣지 않는 경우가 많다.

```text
__pycache__/
.venv/
.env
.ipynb_checkpoints/
```

이유:

- `__pycache__/`: Python이 자동으로 만드는 캐시 파일이다.
- `.venv/`: 가상환경 폴더로, 용량이 크고 컴퓨터마다 다르다.
- `.env`: API key 같은 민감한 정보가 들어갈 수 있다.
- `.ipynb_checkpoints/`: Jupyter가 자동으로 만드는 임시 저장 폴더다.

정리:

```text
Git = 중요한 변경 이력을 기록하는 도구
.gitignore = Git이 무시해야 할 파일 목록
```

현재 학습 프로젝트는 대부분 Markdown 노트라서 아직 `.gitignore`가 필수는 아니다. Python 실습과 데이터 분석을 시작하면 `.gitignore`를 추가하는 것이 좋다.

## Commit Message Used

```text
docs: initialize AI 30-day learning plan
```

뜻:

```text
문서 성격의 변경이며, 30일 AI 학습 플랜을 처음으로 Git에 기록한다.
```
