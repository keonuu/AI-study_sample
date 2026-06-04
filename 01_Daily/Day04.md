# Day 04 - Git/GitHub 입문

## Today's Goal

Git과 GitHub의 역할, repository, commit, branch, push의 기본 개념을 이해하고 작은 실습을 한다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 4를 따른다.

## Work Log

- Day 1-3 내용을 복습했다.
- Git은 파일 변경 이력을 저장하는 도구이고, GitHub는 Git repository를 온라인에 보관/공유하는 서비스라는 점을 배웠다.
- `repository`, `commit`, `branch`, `push`, `pull`의 기본 의미를 배웠다.
- 현재 학습 폴더 `F:\MyDesktop\AI_30Day_MasterPlan`를 Git repository로 만들었다.
- `git add .`로 현재 파일들을 staging area에 올렸다.
- `git commit -m "docs: initialize AI 30-day learning plan"`으로 첫 commit을 만들었다.
- `git log --oneline -1`로 첫 commit 기록을 확인했다.
- `git status --short`로 commit되지 않은 변경사항이 없음을 확인했다.

## Day 1-3 Review

### Day 1

```text
AI > Machine Learning > Deep Learning > LLM
```

Agent는 위 계층 안의 단순 모델 종류가 아니라, LLM에 도구, 작업 절차, 상태 관리, 승인/검증 구조를 붙여 실제 작업을 수행하게 만든 시스템이다.

### Day 2

좋은 질문은 작업 지시서에 가깝다. 좋은 질문에는 목표, 현재 수준, 입력 자료, 원하는 출력, 제약 조건, 검증 기준이 포함되어야 한다.

### Day 3

명령어는 항상 현재 작업 위치를 기준으로 실행된다. 상대 경로는 현재 위치에 따라 의미가 달라지고, 절대 경로는 현재 위치와 상관없이 같은 파일을 가리킨다.

## Git Concepts

Git:

```text
내 컴퓨터에서 파일 변경 이력을 관리하는 도구
```

GitHub:

```text
Git repository를 온라인에 보관하고 공유하는 서비스
```

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

## Commands Practiced

현재 폴더를 Git repository로 만든다.

```powershell
git init
```

Git이 현재 어떤 파일 상태를 보고 있는지 확인한다.

```powershell
git status --short
```

현재 폴더의 모든 변경사항을 staging area에 올린다.

```powershell
git add .
```

staging area에 올라간 변경사항을 하나의 commit으로 기록한다.

```powershell
git commit -m "docs: initialize AI 30-day learning plan"
```

가장 최근 commit을 한 줄로 확인한다.

```powershell
git log --oneline -1
```

## Actual Result

첫 commit:

```text
ce8e398 docs: initialize AI 30-day learning plan
```

commit 결과:

```text
37 files changed
1782 insertions
```

이 commit은 30일 학습 플랜, Day01-Day30 파일, 개념 노트, 참고 문서를 첫 저장 지점으로 기록했다.

## Important Notes

- `git add`는 commit이 아니다. 다음 commit에 넣을 파일을 고르는 단계다.
- `git commit`은 실제 저장 지점을 만드는 단계다.
- `git status --short`가 아무것도 출력하지 않으면 commit되지 않은 변경사항이 없다는 뜻이다.
- 개발자는 보통 의미 있는 작업 단위가 끝났을 때 commit한다.
- Codex는 기본적으로 직접 commit하지 않고, 사용자가 승인했을 때만 commit한다.

## What Is .gitignore?

`.gitignore`는 Git에게 "이 파일들은 Git 기록에 넣지 말라"고 알려주는 설정 파일이다.

예를 들어 Python을 공부하다 보면 다음 같은 파일이나 폴더가 생길 수 있다.

```text
__pycache__/
.venv/
.env
.ipynb_checkpoints/
```

이런 파일들은 보통 코드나 학습 노트의 핵심 내용이 아니거나, 환경마다 달라지거나, 민감한 정보를 담을 수 있다. 그래서 Git에 기록하지 않는 편이 좋다.

즉:

```text
Git = 중요한 변경 이력을 기록하는 도구
.gitignore = Git이 무시해야 할 파일 목록
```

현재 프로젝트는 아직 대부분 Markdown 노트이므로 `.gitignore` 파일을 바로 만들 필요는 크지 않다. Day 5 이후 Python 파일, 가상환경, 임시 실행 결과가 생기면 `.gitignore`를 만드는 것이 좋다.

## LLM Wiki Note Candidate

Title: Git/GitHub 입문

Tags: `Git`, `GitHub`, `Repository`, `Commit`, `Staging`, `Beginner`

Summary:

Git은 파일 변경 이력을 저장하는 도구이고, GitHub는 Git repository를 온라인에 보관/공유하는 서비스다. `git init`은 현재 폴더를 Git repository로 만들고, `git add`는 다음 commit에 넣을 파일을 staging area에 올리며, `git commit`은 staging된 변경사항을 실제 저장 지점으로 기록한다.

## Questions For Next Time

1. Python 파일은 어떻게 실행하는가?
2. 변수와 자료형은 무엇인가?
3. Python 코드를 Git으로 관리하면 어떤 장점이 있는가?
