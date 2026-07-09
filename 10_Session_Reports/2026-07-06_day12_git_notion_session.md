# 2026-07-06 Session Report - Day 12 Git/GitHub And Notion Study Workflow

## Purpose

이번 세션은 AI 30-Day MasterPlan의 Day 12 Git/GitHub 학습을 시작하고, 동시에 Notion을 장기 복습 시스템으로 쓰기 위한 형식을 점검한 세션이다.

## Session Status

- Day 12는 완료가 아니라 진행 중이다.
- Git/GitHub 개념 학습은 branch, commit message, staging area, push, Pull Request까지 진행했다.
- 세션 마무리 검증에서 현재 branch가 `day12-git-practice`인 것을 확인했다.
- 이번 정리 commit은 `day12-git-practice` branch에 남긴다.
- push와 Pull Request 생성은 아직 실행하지 않았다.
- 세션 마지막에 다음 세션에서 이어보기 위해 repo 기록과 리포트를 남겼다.

## Notion Work Completed Earlier In This Session

- `AI 개발하기 > AI 공부하기 30일 plan` 아래에 `AI 30-Day Study Review` database를 만들었다.
- Day 1-11 row를 생성하고, 각 Day별 복습 상태와 source 정보를 넣었다.
- Day 11 기존 페이지는 유지했다.
- Day 11.1 실험용 상세 페이지를 새로 만들어 상세 노트 형식을 테스트했다.
- Day 11.1은 예시를 toggle 형태로 넣는 방식이 보기 좋다고 판단했다.
- Notion에서는 GitHub alert 문법인 `> [!CAUTION]`보다 오답/교정 toggle 방식이 더 안정적이라고 판단했다.

## Notion Note Format Decision

앞으로 Notion 학습 노트는 다음 구조를 기본형으로 쓴다.

```text
Day N
- 오늘 목표
- 이전 Day 복습
- 핵심 개념
- 예시 toggle
- 실습 / 코드 / 명령어
- 내가 헷갈린 지점
- 오답/교정 toggle
- 복습 질문
- Repo source / commit / practice files
```

Repo Markdown에서는 GitHub alert 형식을 유지한다.

```markdown
> [!CAUTION]
> [오답/교정] 교정 내용
```

Notion에서는 가능하면 오답을 toggle로 분리한다.

```text
오답 1 - 제목
- 내 답
- 왜 틀렸는지
- 올바른 기준
- 다음에 기억할 문장
```

## Day 12 Concepts Covered

### Branch

- branch는 같은 repo 안의 작업 분기다.
- `master/main`은 안정적인 기준선으로 두고, 새 작업은 branch에서 진행한다.
- branch는 복사본 폴더가 아니라 Git commit 흐름을 갈라 관리하는 방식이다.

### Commit Message

- commit은 단순 저장이 아니라 의미 있는 변경 단위에 이름표를 붙여 기록하는 것이다.
- 좋은 commit message는 변경 종류와 내용을 보여준다.

예:

```text
docs: add day 12 branch and commit lesson
fix: correct raw data folder explanation
feat: add expression summary script
```

### Working Tree, Staging Area, Commit

```text
working tree -> staging area -> commit
```

- working tree: 실제로 고친 파일들
- staging area: 이번 commit에 넣겠다고 고른 변경사항
- commit: staged 변경사항에 이름표를 붙여 현재 branch에 기록한 것

### Push

- `git commit`은 local repo에 기록한다.
- `git push`는 local commit을 GitHub remote repo로 올린다.

```text
local repo  -> 내 컴퓨터의 Git 프로젝트
remote repo -> GitHub의 Git 프로젝트
```

### Pull Request

- PR은 단순 업로드가 아니라 branch 변경사항을 master/main에 합치기 전에 검토하는 공간이다.
- 개인 프로젝트에서는 내가 나를 검토하는 diff 확인 화면이다.
- 팀 프로젝트에서는 팀원/리뷰어가 검토한다.
- 오픈소스에서는 maintainer가 검토한다.

## User Answers And Learning Pattern

### Strong Points

- branch가 master/main을 지키기 위한 실험 공간이라는 점을 잘 이해했다.
- commit은 현재 서 있는 branch에 생긴다는 핵심을 정확히 잡았다.
- push가 remote GitHub 저장소로 올리는 것이라는 점을 정확히 이해했다.
- 개인 프로젝트에서도 PR이 merge 전 점검대 역할을 한다는 점을 잘 이해했다.
- `git switch -c`에서 `switch`와 `-c`의 의미를 분리해서 설명했다.

### Correction Points

> [!CAUTION]
> [오답/교정] `docs`는 `docs/` 폴더만 뜻하지 않는다. commit type으로서 문서 변경을 의미한다.

> [!CAUTION]
> [오답/교정] `git commit`은 master에 합치는 명령이 아니다. 현재 branch에 변경 기록을 남기는 명령이다.

> [!CAUTION]
> [오답/교정] `fork`와 `branch`는 다르다. branch는 같은 repo 안의 작업 분기이고, fork는 다른 사람의 repo를 내 GitHub 계정으로 복사한 별도 repo다.

## Next Session Starting Point

다음 세션에서는 현재 branch와 commit 상태를 먼저 확인한 뒤 실제 Git 실습으로 이어가면 된다.

Recommended sequence:

```powershell
git status --short --branch
```

현재 branch가 `day12-git-practice`이면 그대로 이어가고, 아니라면 branch 상태를 먼저 확인한다. 그다음 작은 파일 또는 Day 12 기록을 수정하고 아래 흐름을 실습한다.

```powershell
git status
git add 01_Daily/Day12.md
git commit -m "docs: update day 12 git practice notes"
```

push/PR은 remote 설정 확인 후 진행한다.

```powershell
git remote -v
```

## Suggested Next Session Prompt

```text
F:\MyDesktop\AI_30Day_MasterPlan 프로젝트에서 이어가자.
10_Session_Reports\2026-07-06_day12_git_notion_session.md 리포트를 먼저 읽고,
Day 12 Git/GitHub 실습을 이어서 진행해줘.
오늘은 branch 상태 확인, git add, commit까지 실습하고,
remote 상태를 확인한 뒤 push/PR은 진행 여부를 판단하자.
```

## Files Updated In This Wrap-Up

```text
01_Daily/Day12.md
02_Concepts/Git_Branch_Workflow.md
10_Session_Reports/2026-07-06_day12_git_notion_session.md
```
