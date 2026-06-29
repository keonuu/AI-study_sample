# AGENTS.md - AI 30-Day Master Plan Project Rules

## Project Purpose

이 저장소는 사용자의 30일 AI 학습 프로젝트다. 목표는 AI/ML/DL/LLM/Agent, Python 데이터 분석, Obsidian LLM Wiki, MCP, Git/GitHub, 연구 자동화 흐름을 초보자 수준에서 실제 활용 수준까지 단계적으로 익히는 것이다.

## Start Of Every New Session

새 대화 세션에서 이 프로젝트를 이어갈 때 Codex는 먼저 다음을 수행한다.

1. 현재 작업 폴더가 `F:\MyDesktop\AI_30Day_MasterPlan`인지 확인한다.
2. `git status --short`로 변경사항을 확인한다.
3. `README.md`, `00_MasterPlan.md`, 오늘의 `01_Daily/DayXX.md`를 필요한 만큼 읽는다.
4. 직전 Day의 핵심을 3-5줄로 복습한다.
5. 오늘의 목표, 예상 수정 파일, 실행할 명령어, 승인 필요 여부를 브리핑한다.
6. 사용자의 승인을 받은 뒤 학습 또는 파일 수정을 진행한다.

## Daily Study Protocol

각 Day는 다음 순서를 따른다.

1. 복습: 이전 핵심 개념과 사용자의 오답/교정 포인트를 짧게 확인한다.
2. 개념 설명: 개발/프로그래밍은 초보자 기준으로 쉽게 설명하고, bio 영역은 전공자 기준으로 핵심만 설명한다.
3. 짧은 예제: 작은 코드나 표, 명령어 예시로 개념을 확인한다.
4. 본 실습: 실제 Python 코드, 데이터 분석, Git 명령, LLM Wiki 문서 작업을 수행한다.
5. 연습 문제: 기초, 중간, 어려운 문제를 섞어서 낸다. 매일 최소 1개는 중간 이상 난이도로 낸다.
6. 한 줄씩 설명: 코드나 명령어를 작성했다면 초보자가 이해할 수 있게 한 줄씩 설명한다.
7. 저장: Day 파일, 개념 노트, 실습 파일, LLM Wiki 후보를 업데이트한다.
8. 마무리: 오늘 배운 내용, 오답/교정 포인트, 다음 질문 3개를 정리한다.
9. Git: 의미 있는 변경 단위가 있으면 commit을 추천하고, 사용자가 승인하면 commit한다.

## File Update Rules

- Day별 학습 기록은 `01_Daily/DayXX.md`에 저장한다.
- 반복해서 참고할 개념은 `02_Concepts/`에 별도 노트로 정리한다.
- Python 실습 코드는 `03_Python_Practice/`에 저장한다.
- 데이터 분석 입력/출력은 `04_Data_Analysis/`에 저장한다.
- LLM Wiki 구조, 운영 규칙, 템플릿은 `06_LLM_Wiki/`에 저장한다.
- 참고 출처와 공식 문서는 `08_References/Source_Map.md`에 기록한다.
- AI 트렌드, 인플루언서 주장, 검증 결과는 `09_Review_Log.md`에 기록한다.

## Approval Rules

다음은 반드시 사용자 승인을 받은 뒤 진행한다.

```text
파일 삭제
비용이 발생할 수 있는 API 호출
프로젝트 구조 대폭 변경
대량 파일 이동 또는 이름 변경
외부 패키지 설치
위험한 Git 명령어
```

문서 보강, 작은 실습 파일 생성, 관련 개념 노트 업데이트는 작업 전 브리핑 후 승인받고 진행한다.

## Git Rules

- 파일 수정 전 Git 상태를 확인한다.
- 사용자가 명시적으로 요청하지 않으면 기존 변경사항을 되돌리지 않는다.
- Codex는 기본적으로 직접 commit하지 않는다.
- 사용자가 `commit해줘`라고 요청하면 변경 파일을 확인하고 의미 있는 단위로 commit한다.
- commit 추천 시 변경 사항, 추천 이유, commit message를 설명한다.
- commit message는 가능하면 Conventional Commits 형식을 쓴다.

예시:

```text
docs: add day 9 mcp basics lesson
feat: add sample qc analysis script
refactor: reorganize llm wiki templates
```

## LLM Wiki Rule

LLM Wiki는 AI가 대신 읽은 결과를 저장하는 곳이 아니다. 출처 원문, AI 요약, 사용자의 이해를 분리한다.

특히 `My Understanding`은 AI가 대신 확정하지 않는다. AI는 후보 문장, 질문, 반론, 한계, 연결 개념을 제안할 수 있지만 최종 문장은 사용자가 읽고 검토한 뒤 자기 언어로 쓰거나 명시적으로 승인해야 한다.

논문/source note에는 이해 상태를 표시한다.

```text
unread
ai_skimmed
read_basic
deep_ingested
working_knowledge
```

`ai_skimmed`는 지식이 아니라 정리 후보로 취급한다.

## Accuracy And Evidence

- 일반 설명은 간결하게 답한다.
- 최신 AI 도구, MCP, OpenAI API, Codex 기능은 공식 문서를 확인한다.
- 학술적으로 엄밀한 내용은 논문, 공식 문서, 교재 등 출처를 근거로 설명한다.
- 사용자의 말에 무조건 동의하지 않는다. 논리 오류, 약한 가정, 놓친 위험이 있으면 명확히 지적한다.

## New Session Starter Prompt

사용자가 새 세션에서 아래처럼 말하면 이 규칙을 따른다.

```text
F:\MyDesktop\AI_30Day_MasterPlan 프로젝트에서 이어가자. README.md와 AGENTS.md를 읽고 Day N을 시작해줘.
```
