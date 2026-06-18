# AI 30-Day Master Plan

## Purpose

이 문서는 30일 동안 AI를 "도구로 잘 쓰는 사람"에서 "AI 기반 학습/연구/자동화 시스템을 설계할 수 있는 사람"으로 성장하기 위한 학습 계획이다.

현실적인 목표는 30일 만에 모든 AI 이론과 모든 도구를 완전히 마스터하는 것이 아니다. 목표는 다음이다.

- AI/ML/DL/LLM/RAG/MCP/Agents/Git/GitHub의 큰 지도를 이해한다.
- Python과 데이터 분석의 기초를 직접 실행해 본다.
- Obsidian 기반 LLM Wiki를 만들고, 학습 내용을 재사용 가능한 지식으로 저장한다.
- MCP와 Agent가 왜 중요한지 이해하고, 안전하게 연결하고 활용하는 감각을 만든다.
- 새로 유행하는 AI 기능이나 "고급 스킬"을 맹목적으로 따라 하지 않고, 공식 문서와 직접 실험으로 검증하는 습관을 만든다.

## Folder Structure

```text
AI_30Day_MasterPlan
├── 00_MasterPlan.md
├── 01_Daily
│   ├── Day01.md ... Day30.md
│   └── Day_Template.md
├── 02_Concepts
├── 03_Python_Practice
├── 04_Data_Analysis
├── 05_ML_DL
├── 06_LLM_Wiki
├── 07_Agents_Automation
├── 08_References
│   └── Source_Map.md
└── 09_Review_Log.md
```

## Daily Protocol

매일 Codex에게 다음처럼 말한다.

```text
N일차 시작하자. 오늘은 00_MasterPlan.md 기준으로 진행해줘.
```

매일 진행 순서:

1. 오늘의 개념을 쉬운 설명으로 이해한다.
2. 짧은 예제로 확인한다.
3. 직접 실습한다.
4. 결과를 해당 Day 파일에 정리한다.
5. LLM Wiki에 남길 핵심 노트를 만든다.
6. 다음날 이어갈 질문 3개를 작성한다.

## Practice Difficulty Protocol

매일 학습 점검 문제는 쉬운 문제만 반복하지 않고 난이도를 단계적으로 올린다.

1. 기초 문제: 출력 예측, 문법 확인, 한 줄 의미 설명
2. 중간 문제: 조건문, 반복문, 함수, dictionary 등 여러 개념을 조합
3. 상급 문제: 버그가 있는 코드를 고치거나 작은 분석 로직을 직접 설계
4. 실전 문제: 힌트를 줄이고 작은 데이터 분석 또는 자동화 과제를 끝까지 수행

초보 단계에서는 개념 이해를 놓치지 않기 위해 기초 문제로 시작하되, 매일 마지막에는 최소 1개의 중간 또는 상급 문제를 포함한다.

## Source And Evidence Policy

- 일반적인 개념 설명은 쉬운 설명을 우선한다.
- 학술적으로 엄밀한 내용은 논문, 공식 문서, 교재 등 출처를 확인한다.
- 최신 AI 도구/기능은 공식 문서를 먼저 확인한다.
- Instagram, YouTube, X, 블로그에서 본 AI 팁은 "아이디어 후보"로만 취급하고, 공식 문서 또는 직접 실험으로 검증한다.
- 비용이 발생할 수 있는 API 사용은 실행 전에 반드시 승인받는다.

## Phase 1: Beginner Foundation, Days 1-10

초보자 단계의 목표는 AI의 전체 지도를 만들고, Python/터미널/Git/Obsidian/LLM Wiki의 기초 사용 흐름을 잡는 것이다.

| Day | Topic | Outcome |
|---|---|---|
| 1 | AI, ML, DL, LLM, Agent의 차이 | AI 개념 지도와 용어 노트 |
| 2 | Codex/ChatGPT를 학습 파트너로 쓰는 법 | 좋은 질문 템플릿과 나쁜 질문 예시 |
| 3 | 파일, 폴더, 터미널, VS Code, 실행 환경 | 내 컴퓨터 개발 환경 지도 |
| 4 | Git/GitHub 입문 | repository, commit, branch, push 개념 노트 |
| 5 | Python 기초 1: 변수, 자료형, 실행 | 짧은 Python 예제 파일 |
| 6 | Python 기초 2: 조건문, 반복문, 함수 | 작은 계산 프로그램 |
| 7 | pandas/numpy/matplotlib 기초 | 작은 표 데이터 읽기와 그래프 |
| 8 | Obsidian LLM Wiki 구조 설계 | Wiki 폴더 구조와 노트 템플릿 |
| 9 | MCP 입문 | host/client/server/tools/resources/prompts 개념 지도 |
| 10 | 초보 미니 프로젝트 | 작은 데이터 분석 리포트와 Wiki 노트 |

### Day 1 Details

- AI, ML, DL, LLM, Agent를 구분한다.
- "모델", "프롬프트", "컨텍스트", "도구", "워크플로우"를 이해한다.
- 현재 AI 흐름이 단순 채팅에서 도구 사용, 검색, 자동화, Agent로 이동하고 있음을 이해한다.

### Day 2 Details

- Codex에게 좋은 질문을 하는 법을 배운다.
- "목표, 현재 상태, 입력 자료, 원하는 출력, 제약 조건"을 포함한 질문 템플릿을 만든다.
- AI 답변을 무조건 믿지 않고 검증하는 습관을 만든다.

### Day 3 Details

- Windows PowerShell, Ubuntu/WSL, VS Code, 파일 경로를 이해한다.
- 절대 경로와 상대 경로를 배운다.
- "어디에서 명령어를 실행해야 하는가"를 항상 확인하는 습관을 만든다.

### Day 4 Details

- Git은 변경 이력을 저장하는 도구이고, GitHub는 그 이력을 온라인에 보관/공유하는 서비스임을 이해한다.
- `git status`, `git add`, `git commit`, `git log`의 의미를 배운다.
- 실제 연습용 폴더에서 commit을 한 번 만들어 본다.

### Day 5 Details

- Python 파일 실행 방식, 변수, 문자열, 숫자, 리스트, 딕셔너리를 배운다.
- 코드 한 줄이 어떤 입력을 받아 어떤 출력을 만드는지 읽는 연습을 한다.

### Day 6 Details

- 조건문, 반복문, 함수의 필요성을 이해한다.
- 같은 코드를 반복하지 않기 위해 함수를 쓰는 이유를 배운다.

### Day 7 Details

- pandas는 표 데이터, numpy는 숫자 배열, matplotlib은 그래프를 다루는 도구로 이해한다.
- 작은 CSV를 읽고 요약 통계와 그래프를 만든다.

### Day 8 Details

- Obsidian을 단순 노트 앱이 아니라 개인 지식 데이터베이스로 설계한다.
- concept note, paper note, code note, question note 템플릿을 만든다.

### Day 9 Details

- MCP는 LLM 앱이 외부 도구와 데이터에 연결되는 표준 방식임을 이해한다.
- host, client, server, tools, resources, prompts를 구분한다.
- MCP를 무작정 설치하지 않고 권한과 보안 위험을 먼저 이해한다.

### Day 10 Details

- 작은 데이터셋을 불러오고, 요약하고, 그래프를 만들고, 결과를 Wiki에 정리한다.
- "AI와 함께 공부한 내용"을 재사용 가능한 노트로 바꾼다.

## Phase 2: Intermediate AI Learning And Bio Data Analysis, Days 11-20

중급 단계의 목표는 데이터 분석과 머신러닝의 기본 흐름을 이해하고, LLM Wiki와 MCP를 실제 학습/분석 흐름에 연결하는 것이다.

| Day | Topic | Outcome |
|---|---|---|
| 11 | 재현 가능한 데이터 분석 프로젝트 구조 | raw/processed/results/notebooks 구조 |
| 12 | Git/GitHub 실습 | branch, commit message, push, pull request 연습 |
| 13 | EDA와 시각화 | 데이터 요약 리포트 |
| 14 | Bioinformatics 데이터 형태 | sample x feature, gene expression matrix 노트 |
| 15 | 머신러닝 기본 구조와 Python class/method 입문 | feature, label, train/test split, model 객체 사용 노트 |
| 16 | scikit-learn 첫 모델 | baseline model 실습 |
| 17 | 모델 평가와 데이터 누수 | accuracy, precision, recall, leakage 정리 |
| 18 | Embedding, vector search, RAG | LLM Wiki 검색 구조 설계 |
| 19 | MCP 연결 실습 | 안전한 local MCP 연결 또는 연결 설계 |
| 20 | 중급 미니 프로젝트 | bio 데이터 분석 + ML baseline + Wiki 정리 |

### Day 11 Details

- 분석 프로젝트는 데이터를 덮어쓰지 않고, raw와 processed를 분리해야 함을 배운다.
- notebook, script, output, report의 역할을 구분한다.

### Day 12 Details

- 실제로 GitHub 저장소 하나를 만들고, branch와 pull request 흐름을 연습한다.
- commit message를 왜 작은 단위로 쓰는지 이해한다.

### Day 13 Details

- 평균, 분산, 분포, outlier, missing value를 데이터 분석 관점에서 다룬다.
- 표와 그래프를 같이 보며 데이터의 이상한 점을 찾는다.

### Day 14 Details

- 생명과학 데이터에서 sample, feature, gene, read, count, metadata의 의미를 정리한다.
- NGS mapping 경험을 데이터 분석 흐름과 연결한다.

### Day 15 Details

- 머신러닝은 입력 feature에서 target label을 예측하는 함수 근사 문제로 이해한다.
- train/test split을 왜 하는지 배운다.
- scikit-learn의 `model.fit()`과 `model.predict()`를 읽기 위해 Python class, object, method의 최소 개념을 배운다.
- 이 단계의 목표는 class를 직접 잘 설계하는 것이 아니라, class로 만들어진 도구를 정확히 읽고 사용하는 것이다.

### Day 16 Details

- scikit-learn으로 첫 baseline model을 만든다.
- 복잡한 모델보다 단순한 기준 모델을 먼저 만드는 이유를 배운다.

### Day 17 Details

- accuracy만 보면 위험한 경우를 이해한다.
- precision, recall, F1, confusion matrix를 생명과학 예시와 연결한다.
- 데이터 누수는 모델 성능을 가짜로 좋게 만드는 핵심 위험임을 배운다.

### Day 18 Details

- embedding은 문장/문서를 숫자 벡터로 바꾸는 방식임을 이해한다.
- RAG는 "모델이 외부 지식을 검색한 뒤 답하는 구조"로 이해한다.
- LLM Wiki를 검색 가능한 지식 저장소로 만들 때 필요한 구조를 설계한다.

### Day 19 Details

- MCP 서버를 연결할 때 tool 이름, 권한, 접근 가능한 파일 범위, 비용 발생 가능성을 확인한다.
- 안전한 범위에서 filesystem 또는 documentation MCP 연결을 실습하거나, 설치가 부담되면 설계만 한다.

### Day 20 Details

- 작은 bio 관련 데이터셋 또는 예제 데이터를 분석한다.
- 분석 결과, 코드, 개념 노트를 서로 연결한다.

## Phase 3: Advanced Agents And Workflow Automation, Days 21-30

고급 단계의 목표는 Agent, tool calling, MCP, Codex Skills, 자동화, 평가, 보안을 묶어 실제 연구/학습 업무 자동화 설계를 만드는 것이다.

| Day | Topic | Outcome |
|---|---|---|
| 21 | LLM API, Responses API, tool calling 개념 | API/도구 호출 흐름도 |
| 22 | Agent 설계 기초 | task, tool, memory, state, approval 설계 |
| 23 | Agents SDK, tracing, guardrails, evals | Agent 디버깅/평가 노트 |
| 24 | Codex 고급 활용: AGENTS.md, Skills, multi-agent | 개인 Codex 사용 규칙 개선안 |
| 25 | MCP 고급: tool design, permissions, security | 안전한 MCP 체크리스트 |
| 26 | 논문 정리 자동화 | paper-to-wiki workflow 설계 |
| 27 | 데이터 분석 자동화 | CSV-to-report workflow 설계 |
| 28 | LLM Wiki Assistant 설계 | retrieval, citation, evidence map 설계 |
| 29 | 개인 연구 Agent 설계 | bio/ML 학습 Agent 명세서 |
| 30 | 최종 프로젝트 | 내 연구/학습 자동화 Agent 프로토타입 계획 |

### Day 21 Details

- LLM API는 앱이나 스크립트에서 모델을 호출하는 방법임을 이해한다.
- tool calling은 모델이 직접 일을 끝내는 것이 아니라, 필요한 도구 호출을 제안하고 실행 결과를 받아 답하는 구조임을 이해한다.
- 비용이 발생할 수 있는 API는 실제 실행 전에 반드시 승인한다.

### Day 22 Details

- Agent는 "목표를 이해하고, 계획을 세우고, 도구를 사용하고, 중간 상태를 관리하는 시스템"으로 이해한다.
- 모든 자동화에는 사람 승인 지점이 필요함을 배운다.

### Day 23 Details

- tracing은 Agent가 어떤 판단과 도구 호출을 했는지 추적하는 기록이다.
- guardrails는 위험하거나 잘못된 행동을 막는 장치다.
- evals는 Agent가 잘하는지 반복적으로 검사하는 테스트다.

### Day 24 Details

- `AGENTS.md`는 Codex가 프로젝트에서 따라야 할 규칙 문서다.
- Skills는 반복되는 작업 방식을 재사용 가능한 절차로 저장하는 방식이다.
- multi-agent는 여러 에이전트가 병렬로 작업하는 방식이지만, 초보자는 무작정 쓰기보다 작업 분해와 검증 기준을 먼저 배워야 한다.

### Day 25 Details

- MCP tool은 강력하지만 파일 접근, 명령 실행, 외부 API 호출 권한 때문에 위험할 수 있다.
- least privilege, allowlist, read-only mode, human approval, logging을 체크리스트로 만든다.
- prompt injection과 tool poisoning 위험을 이해한다.

### Day 26 Details

- 논문 PDF 또는 초록을 읽고 핵심 주장, 실험 방법, 결과, 한계를 추출하는 workflow를 설계한다.
- 인용 가능한 문장과 해석을 분리한다.

### Day 27 Details

- CSV나 실험 데이터를 넣으면 기초 통계, 그래프, 이상치, 리포트를 생성하는 workflow를 설계한다.
- 분석 결과와 코드, 노트가 연결되게 만든다.

### Day 28 Details

- LLM Wiki Assistant는 답변보다 "근거가 있는 답변"이 중요하다.
- retrieval, citation, evidence map, contradiction check 구조를 설계한다.

### Day 29 Details

- 개인 연구 Agent가 할 일과 하지 말아야 할 일을 명확히 정한다.
- 예: 논문 요약, 용어 설명, 코드 초안, 분석 체크리스트 생성은 가능. 근거 없는 학술 주장, 무승인 API 비용 발생, 위험한 파일 조작은 금지.

### Day 30 Details

- 30일 동안 만든 노트, 코드, Wiki 구조, 자동화 설계를 모아 최종 리뷰한다.
- 다음 30일 학습 계획을 만든다.

## Trend Radar

AI 커뮤니티나 인플루언서가 소개하는 기능은 다음 기준으로 평가한다.

1. 이 기능은 어떤 문제를 해결하는가?
2. 공식 문서나 원출처가 있는가?
3. 직접 작은 예제로 재현 가능한가?
4. 비용, 보안, 개인정보 위험은 없는가?
5. 내 LLM Wiki, bioinformatics, 데이터 분석 목표와 연결되는가?

매주 최소 2개 트렌드를 골라 `09_Review_Log.md`에 정리한다.

현재 30일 플랜에 포함된 핵심 흐름:

- LLM과 prompting
- Python과 데이터 분석
- Git/GitHub
- Obsidian 기반 LLM Wiki
- RAG와 vector search
- MCP
- tool calling
- Agents
- tracing, guardrails, evals
- Codex AGENTS.md와 Skills
- multi-agent workflow
- 논문 정리 자동화
- 데이터 분석 자동화
- Agent 보안과 승인 구조

## Reference Baseline

아래 문서는 계획 수립 시 기준으로 삼은 공식/준공식 문서다. 실제 학습일에는 필요한 문서를 다시 확인한다.

- Model Context Protocol specification: https://modelcontextprotocol.io/specification/latest
- MCP architecture: https://modelcontextprotocol.io/docs/learn/architecture
- OpenAI Responses API: https://platform.openai.com/docs/api-reference/responses
- OpenAI Agents guide: https://developers.openai.com/api/docs/guides/agents
- OpenAI Agents SDK MCP guide: https://openai.github.io/openai-agents-python/mcp/
- OpenAI Codex overview: https://openai.com/codex/
- OpenAI Codex app announcement: https://openai.com/index/introducing-the-codex-app/
- GitHub Git getting started: https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git
