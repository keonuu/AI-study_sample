# Git Branch Workflow

## Core Idea

Git branch workflow는 안정적인 `master/main`을 직접 흔들지 않고, 새 branch에서 작업한 뒤 검토 후 합치는 흐름이다.

## Core Flow

```text
master/main
  -> create branch
  -> edit files
  -> git add
  -> git commit
  -> git push
  -> pull request
  -> merge
```

## Key Ideas

- repository(repo)는 Git이 관리하는 프로젝트 폴더다.
- local repo는 내 컴퓨터에 있는 저장소이고, remote repo는 GitHub 같은 원격 저장소다.
- branch는 같은 repo 안의 별도 작업선이다.
- commit은 현재 내가 서 있는 branch에 기록된다.
- `git add`는 선택한 변경사항을 staging area에 올린다.
- `git commit`은 staged 변경사항을 현재 branch에 기록한다.
- `git push`는 local commit을 GitHub 같은 remote repository로 올린다.
- Pull Request는 branch를 `master/main`에 합치기 전 변경사항을 검토하는 공간이다.

## Branch And Fork

```text
branch = 같은 repo 안의 작업 분기
fork   = 다른 사람 repo를 내 GitHub 계정으로 복사한 별도 repo
```

AI 30-Day MasterPlan 같은 개인 학습 repo에서는 보통 fork보다 branch를 사용한다.

## Day 12 Practice Branch

```powershell
git switch -c day12-git-practice
```

이 명령은 `day12-git-practice`라는 새 branch를 만들고 그 branch로 이동한다.
