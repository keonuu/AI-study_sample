# AI 30-Day Master Plan

이 프로젝트는 AI, Python, 데이터 분석, Obsidian LLM Wiki, MCP, Agents를 30일 동안 단계적으로 학습하기 위한 개인 학습 저장소다.

## How To Continue In A New Codex Session

새 대화 세션에서 이어갈 때는 Codex에게 아래처럼 말한다.

```text
F:\MyDesktop\AI_30Day_MasterPlan 프로젝트에서 이어가자. 먼저 README.md와 AGENTS.md를 읽고, Git 상태를 확인한 뒤 Day N을 시작해줘. 시작 전에 Day N의 계획과 수정/실행할 파일을 브리핑하고 내 승인을 받은 뒤 진행해줘.
```

예시:

```text
F:\MyDesktop\AI_30Day_MasterPlan 프로젝트에서 이어가자. Day 9 MCP 학습을 시작하자. 먼저 README.md와 AGENTS.md를 읽고, Git 상태를 확인한 뒤 Day 8 핵심만 짧게 복습하고 Day 9 계획을 브리핑해줘.
```

## Short Start Command

새 세션에서는 길게 설명하지 않아도 된다. 아래처럼 짧게 시작한다.

```text
AI 30일 플랜 Day N 시작
```

Codex는 이 말을 들으면 다음처럼 처리해야 한다.

```text
1. F:\MyDesktop\AI_30Day_MasterPlan 프로젝트 규칙을 따른다.
2. Git 상태와 오늘 Day 파일만 최소한으로 확인한다.
3. 파일을 먼저 작성하지 않는다.
4. 과외식으로 개념 하나를 설명하고 질문 하나를 낸 뒤 기다린다.
5. Day 마지막에 사용자가 요청하면 그때 학습 기록을 저장하고 commit을 추천한다.
```

금지되는 흐름:

```text
Day 파일을 먼저 채우기
개념 노트를 먼저 만들기
문제와 정답을 한 번에 다 쓰기
사용자 답변 없이 학습을 끝낸 것처럼 기록하기
```

## Current Learning Style

매일 학습은 다음 순서로 진행한다.

1. 이전 Day 핵심을 짧게 복습한다.
2. 오늘의 목표를 `00_MasterPlan.md`와 `01_Daily/DayXX.md` 기준으로 확인한다.
3. Codex가 오늘 할 일, 수정할 파일, 실행할 명령어, 필요한 승인을 먼저 브리핑한다.
4. 사용자가 승인하면 학습을 시작한다.
5. 개념을 먼저 설명한다.
6. 짧은 예제로 확인한다.
7. 직접 실습한다.
8. 쉬운 문제, 중간 문제, 어려운 문제를 섞어 이해도를 점검한다.
9. 오늘 배운 내용을 Day 파일과 관련 개념 노트에 정리한다.
10. 필요하면 Python 실습 파일, 데이터 파일, LLM Wiki 템플릿을 업데이트한다.
11. 마지막에 변경 파일, 배운 내용, 오답/교정 포인트, 다음 질문을 요약한다.
12. 의미 있는 변경 단위가 생기면 Codex가 Git commit을 추천한다.

## Tutor-Style Learning Protocol

이 프로젝트의 핵심은 Codex가 단순히 답을 주는 것이 아니라, 옆에서 과외 선생님처럼 학습을 이끄는 것이다.

하루 학습은 전체 내용을 한 번에 설명하지 않는다. 중요한 개념을 작은 단위로 나누고, 각 단위마다 아래 흐름을 반복한다.

```text
1. 개념 하나를 아주 쉽게 설명한다.
2. 왜 필요한지 실제 사용 맥락을 설명한다.
3. 짧은 예시를 보여준다.
4. 사용자에게 쉬운 확인 문제를 낸다.
5. 사용자의 답을 채점하고, 맞은 부분과 틀린 부분을 구분한다.
6. 필요하면 꼬리 질문이나 추가 예제를 낸다.
7. 이해가 확인되면 다음 개념으로 넘어간다.
```

문제 난이도는 다음처럼 섞는다.

```text
기초: 용어 뜻, 출력 예측, 한 줄 코드 의미
중간: 여러 개념을 조합한 작은 문제
어려움: 오류 찾기, 직접 설계, 실전 상황 판단
```

Day가 끝나면 단순 요약만 남기지 않는다. 오늘 어떤 개념을 배웠고, 어떤 문제를 풀었고, 어떤 답을 잘했고, 어떤 부분을 교정했는지 학습 기록으로 남긴다.

## Folder Map

```text
00_MasterPlan.md                  전체 30일 계획
01_Daily/DayXX.md                 매일 학습 기록
02_Concepts/                      재사용 가능한 개념 노트
03_Python_Practice/               Python 실습 코드
04_Data_Analysis/                 CSV, 그래프, 분석 결과
05_ML_DL/                         머신러닝/딥러닝 실습 자료
06_LLM_Wiki/                      Obsidian LLM Wiki 설계와 템플릿
07_Agents_Automation/             Agent/자동화 실습 자료
08_References/Source_Map.md       참고 출처 지도
09_Review_Log.md                  복습, 트렌드 검증, 주간 리뷰
AGENTS.md                         Codex가 이 프로젝트에서 따라야 할 규칙
README.md                         새 세션 시작 안내서
```

## Daily Output Checklist

각 Day가 끝날 때 가능하면 아래가 남아 있어야 한다.

```text
1. 01_Daily/DayXX.md 업데이트
2. 02_Concepts/ 관련 개념 노트 업데이트
3. 필요한 경우 03_Python_Practice 또는 04_Data_Analysis 실습 파일 저장
4. 오늘의 질문, 오답, 교정 포인트 정리
5. Git commit 추천 또는 사용자가 승인하면 commit 실행
```

## Git Habit

Codex는 기본적으로 바로 commit하지 않는다. 다만 학습 기록, 개념 노트, 실습 파일이 의미 있는 단위로 정리되면 commit을 추천한다.

추천 형식:

```text
지금 commit하면 좋다.
이유: Day N 학습 기록과 관련 실습 파일이 한 단위로 정리되었기 때문.
추천 commit message: docs: add day N mcp basics lesson
```

사용자가 `commit해줘`라고 승인하면 그때 `git add`와 `git commit`을 실행한다.

## Important Rule

이 프로젝트의 목적은 AI가 대신 공부한 결과를 쌓는 것이 아니다. AI의 도움을 받아 사용자가 직접 이해하고, 검토하고, 자기 언어로 정리한 지식을 쌓는 것이다.
