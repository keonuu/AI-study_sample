# Day 12 - Git/GitHub 실습

## Today's Goal

branch, commit message, push, pull request 흐름을 실제로 연습한다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 12를 따른다.

## Work Log

- Day 11 복습 후 Day 12 Git/GitHub 실습을 시작했다.
- 오늘은 파일을 먼저 작성하지 않고 과외식으로 branch, commit message, staging area, push, Pull Request 개념을 하나씩 확인했다.
- branch는 `master/main`을 안정적인 기준선으로 두고, 새 작업을 분리해서 실험하는 작업선임을 학습했다.
- 사용자는 `master/main`을 지키기 위해 새 branch에서 개발하고 검증 후 merge하는 흐름을 정확히 설명했다.
- commit message는 단순한 저장 문구가 아니라 의미 있는 변경 단위에 붙이는 이름표임을 학습했다.
- `docs:`는 반드시 `docs/` 폴더를 뜻하는 것이 아니라 문서 성격의 변경을 의미하는 commit type임을 교정했다.
- Git의 기본 흐름 `working tree -> staging area -> commit`을 학습했다.
- `git add`는 GitHub 업로드가 아니라 이번 commit에 포함할 변경사항을 staging area에 올리는 명령임을 확인했다.
- `git commit`은 master에 합치는 명령이 아니라 현재 서 있는 branch에 변경 기록을 남기는 명령임을 교정했다.
- `git push`는 local repo의 commit을 GitHub remote repo로 올리는 명령임을 학습했다.
- repo는 Git이 관리하는 프로젝트 저장소이며, local repo는 내 컴퓨터의 프로젝트, remote repo는 GitHub의 프로젝트 저장소로 이해했다.
- branch와 fork를 구분했다. branch는 같은 repo 안의 작업 분기이고, fork는 GitHub에서 남의 repo를 내 계정으로 복사한 별도 repo다.
- Pull Request는 단순 업로드가 아니라 branch의 변경사항을 master/main에 합치기 전에 검토 요청하는 공간임을 학습했다.
- 개인 프로젝트에서도 PR은 merge 전 변경 파일과 diff를 스스로 점검하는 검토 화면으로 의미가 있음을 확인했다.
- `git switch -c day12-git-practice`는 새 branch를 만들고 그 branch로 이동하는 명령임을 학습했다.
- 세션 마무리 시점에 현재 branch가 `day12-git-practice`인 것을 확인했다. 이번 정리 commit은 이 branch에 남기고, push와 Pull Request는 아직 실행하지 않았다.
- 이어진 실습에서 `git add`는 새 파일 변경을 만들어내는 명령이 아니라, 이미 생긴 변경사항을 staging area에 올리는 명령임을 다시 확인했다.

## Questions And Answers

### Q1. Git/GitHub 실습에서 더 좋은 흐름은?

```text
A. master에서 바로 여러 파일을 고치고, 잘못되면 나중에 기억으로 되돌린다.
B. 새 branch를 만들고, 그 branch에서 실험한 뒤, 괜찮으면 master에 합친다.
```

사용자 답변: B. master를 안정적으로 지키면서 새로운 기능 실험이나 테스트를 하려면 새 branch를 판 뒤 개발하고, 안정성을 확인하고 merge하는 것이 좋다.

피드백: 정확함. `master/main`은 안정적인 기준선이고, feature/practice branch는 실험과 작업 공간이다.

### Q2. 더 좋은 commit message는?

```text
A. update files
B. docs: add day 12 branch and commit lesson
```

사용자 답변: B. 어떤 파일/내용을 바꿨는지 보이고, branch와 commit lesson을 추가했다는 의미가 보인다.

피드백: 방향은 정확함.

> [!CAUTION]
> [오답/교정] `docs`는 꼭 `docs/` 폴더를 뜻하는 것이 아니다. commit의 종류가 문서 변경이라는 뜻이다. 예를 들어 `README.md`, `01_Daily/Day12.md`, `02_Concepts/Git_Branch.md`를 수정해도 commit type은 `docs`가 될 수 있다.

### Q3. `git add`의 역할은?

```text
A. 파일을 GitHub에 업로드한다.
B. 이번 commit에 포함할 변경사항을 staging area에 올린다.
C. branch를 master에 합친다.
```

사용자 답변: B. `git status`로 변경 파일을 보고, 이번 commit에 넣을 내용을 staging area에 올린 뒤 commit한다.

피드백: 핵심은 정확함.

> [!CAUTION]
> [오답/교정] `git commit`은 해당 파일들을 master에 합치는 것이 아니다. `git commit`은 현재 내가 서 있는 branch에 변경 기록을 남기는 것이다. master에 합치는 작업은 나중에 `merge` 또는 Pull Request로 한다.

### Q4. `git push`의 역할은?

```text
A. 내 컴퓨터에서 commit한 내용을 GitHub remote 저장소로 올린다.
B. 변경 파일을 staging area에 올린다.
C. GitHub에서 다른 사람이 만든 변경사항을 내 컴퓨터로 가져온다.
```

사용자 답변: A. push는 GitHub에 올리는 것이므로 remote 저장소로 가는 것이다.

피드백: 정확함.

### Q5. 현재 `day12-practice` branch에 서 있을 때 commit은 어디에 생기는가?

```text
A. master branch
B. day12-practice branch
C. GitHub remote repo에만 생김
```

사용자 답변: B. 지금 서 있는 branch에 생성된다.

피드백: 정확함. commit은 현재 branch에 생긴다.

### Q6. Pull Request의 역할은?

```text
A. local 파일을 staging area에 올리는 작업
B. branch의 변경사항을 master/main에 합치기 전에 검토 요청하는 공간
C. GitHub에서 repo를 내 컴퓨터로 다운로드하는 작업
```

사용자 답변: B. 다만 누구의 검토를 요청하는 것인지 질문했다.

피드백: 정확함. 개인 프로젝트에서는 내가 나를 검토하고, 팀 프로젝트에서는 팀원/리뷰어가 검토하며, 오픈소스에서는 maintainer가 검토한다.

### Q7. 혼자 하는 프로젝트에서도 PR을 만들면 좋은 이유는?

```text
A. PR을 만들면 자동으로 코드가 더 좋아진다.
B. merge 전에 변경 파일과 diff를 한 번에 확인할 수 있다.
C. PR을 만들면 git add가 필요 없어진다.
```

사용자 답변: B. 한 번 더 점검할 수 있다는 의미가 있다.

피드백: 정확함.

### Q8. `git switch -c day12-git-practice`는 무엇을 하는가?

```text
A. GitHub에 파일을 업로드한다.
B. 새 branch를 만들고 그 branch로 이동한다.
C. master branch에 변경사항을 merge한다.
```

사용자 답변: B. `git switch`는 branch를 바꾸고, `-c`는 해당 branch를 만든다는 의미이므로 새 branch를 만들고 이동한다.

피드백: 정확함.

## Correction Points

> [!CAUTION]
> [오답/교정] `docs`는 `docs/` 폴더만 뜻하지 않는다. commit type으로서 문서 변경을 의미한다.

> [!CAUTION]
> [오답/교정] `git commit`은 master에 합치는 명령이 아니다. 현재 branch에 변경 기록을 남기는 명령이다.

> [!CAUTION]
> [오답/교정] `fork`와 `branch`는 다르다. branch는 같은 repo 안의 작업 분기이고, fork는 다른 사람의 repo를 내 GitHub 계정으로 복사한 별도 repo다.

## LLM Wiki Note Candidate

- Title: Git Branch, Commit, Push, Pull Request 기본 흐름
- Tags: `git`, `github`, `branch`, `commit`, `push`, `pull request`, `staging area`
- Summary: Git에서는 local repo에서 branch를 만들어 작업하고, `git add`로 staging area에 올린 뒤, `git commit`으로 현재 branch에 기록한다. `git push`는 local commit을 GitHub remote repo로 올리는 것이며, Pull Request는 branch의 변경사항을 master/main에 merge하기 전 diff와 변경 내용을 검토하는 공간이다.

## Questions For Next Time

1. 현재 `day12-git-practice` branch에 있을 때 commit을 만들면 어느 branch에 기록될까?
2. `git add .`와 `git add 01_Daily/Day12.md`는 어떤 차이가 있을까?
3. Day 12 실습 branch에서 commit을 만든 뒤 master에 합치려면 어떤 순서로 진행해야 할까?
