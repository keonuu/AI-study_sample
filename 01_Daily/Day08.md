# Day 08 - Obsidian LLM Wiki 실전 운영 설계

## Today's Goal

Obsidian을 개인 LLM Wiki로 쓰기 위한 폴더 구조, 노트 템플릿, ingest 규칙, Agent 사용 원칙을 설계한다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 8을 따른다.

## Work Log

- LLM Wiki는 단순한 자동 요약기가 아니라, AI가 참고할 수 있는 개인 연구 지식 시스템으로 이해했다.
- AI가 논문을 ingest해도 지식은 자동으로 생기지 않으며, 사람이 읽고 검토하고 자기 언어로 다시 정리해야 한다는 점을 정리했다.
- Agent 작업은 코드 작성, 논문 요약, 분석 자동화 모두에서 인간 검토가 필수임을 확인했다.
- 논문 Wiki, 분석 Wiki, 원고 Wiki는 목적이 다르므로 같은 구조로 섞지 않는 편이 좋다고 정리했다.
- 일반 ingest와 deep ingest를 구분했다.
- 출처 원문, AI 요약, 내 해석, 질문, 작업 로그를 분리해서 저장해야 함을 배웠다.
- `My Understanding`은 AI가 대신 확정하는 문장이 아니라, 내가 읽고 검토한 뒤 내 언어로 작성하거나 명시적으로 승인한 문장이어야 함을 정리했다.
- 논문 노트에는 내가 실제로 어느 수준까지 읽고 이해했는지 `Understanding status`로 표시해야 함을 배웠다.
- LLM Wiki에서 검색 품질은 계속 점검해야 하며, 작은 Wiki에서는 `rg` 같은 키워드 검색도 실용적일 수 있음을 정리했다.
- 대량 PDF 다운로드는 도서관 정책, 저작권, 라이선스 문제가 생길 수 있으므로 조심해야 한다.
- Obsidian LLM Wiki의 기본 구조와 템플릿 초안을 `06_LLM_Wiki` 폴더에 작성했다.

## Core Idea

LLM Wiki는 다음 세 가지를 분리해서 저장하는 시스템이다.

```text
1. Source: 논문, 문서, 링크, 실험 로그 같은 원자료
2. AI Summary: LLM이 만든 요약과 구조화 결과
3. My Understanding: 내가 검토하고 내 말로 다시 정리한 지식
```

이 세 가지가 섞이면 나중에 어떤 내용이 원문 근거인지, 어떤 내용이 AI의 해석인지, 어떤 내용이 내 판단인지 구분하기 어려워진다.

중요한 원칙:

```text
AI Summary = AI가 정리한 내용
My Understanding = 내가 읽고, 검토하고, 내 언어로 확정한 내용
```

AI는 `My Understanding` 후보, 질문, 반론, 빠진 한계, 연결 가능한 개념을 제안할 수 있다. 하지만 최종 `My Understanding`은 내가 직접 쓰거나, 최소한 내가 읽고 동의한 뒤 저장해야 한다.

## LLM Wiki Is Not One-Click Knowledge

논문 PDF를 넣고 요약을 받는 것만으로는 지식이 생기지 않는다.

좋은 사용 방식:

```text
1. 논문 또는 자료를 ingest한다.
2. AI 요약을 눈으로 읽는다.
3. 이해 안 되는 부분을 질문한다.
4. 중요한 개념을 내 말로 다시 쓴다.
5. 기존 Wiki 노트와 연결한다.
6. 새 질문과 다음 읽을 자료를 남긴다.
```

나쁜 사용 방식:

```text
PDF 업로드 -> 요약 생성 -> 읽지 않음 -> 안다고 착각
```

## Understanding Status

논문 노트에는 이해 수준을 표시한다.

```text
unread = 아직 읽지 않음
ai_skimmed = AI 요약만 받은 상태
read_basic = 내가 요약을 읽고 핵심을 확인한 상태
deep_ingested = 기존 Wiki와 연결하고 질문까지 정리한 상태
working_knowledge = 내 연구/분석에 적용할 수 있을 정도로 정리한 상태
```

`ai_skimmed` 상태의 노트는 참고 자료일 뿐, 내가 이해한 지식으로 취급하지 않는다.

## General Ingest vs Deep Ingest

### General Ingest

자료 하나를 읽고 기본 정보를 정리한다.

```text
핵심 질문, 배경, 방법, 결과, 한계, 중요 figure/table, 내가 이해한 요약
```

### Deep Ingest

자료 하나를 기존 Wiki와 연결해 지식 네트워크로 만든다.

```text
기존 개념 노트 연결, 비슷한 주장 또는 반대 주장 찾기, method 비교,
새 질문 도출, 다음에 읽을 key reference 후보 정리, 내 연구/분석 프로젝트 적용 가능성 평가
```

## Wiki Types

### Paper Wiki

논문, 리뷰, preprint, reference를 정리한다.

```text
목적: 연구 배경과 근거 축적
핵심: 출처, 주장, 근거, 한계
```

### Analysis Wiki

데이터 분석 프로젝트를 정리한다.

```text
목적: 분석 재현성과 의사결정 기록
핵심: 데이터 위치, 코드, parameter, 실행 로그, 결과 해석
```

### Manuscript Wiki

원고 작성과 figure/storyline을 정리한다.

```text
목적: 논리 전개와 글쓰기 재사용
핵심: figure message, paragraph plan, reviewer response, 문장 후보
```

## Proposed Structure

```text
My_LLM_Wiki
├── 01_raw
│   ├── papers
│   ├── web
│   └── notes
├── 02_wiki
│   ├── concepts
│   ├── sources
│   ├── projects
│   ├── questions
│   └── index.md
├── 03_meta
│   ├── log.md
│   ├── operating_rules.md
│   └── templates
└── AGENTS.md
```

핵심 원칙:

```text
01_raw = 원자료, 가능한 한 수정하지 않는다.
02_wiki = AI와 사람이 함께 정리한 지식 layer
03_meta = 운영 규칙, 템플릿, 작업 로그
```

## Agent Rules

Agent가 Wiki를 사용할 때는 다음 순서를 따른다.

```text
1. 먼저 Wiki index를 읽는다.
2. 관련 concept/source/project note를 찾는다.
3. 근거가 부족하면 raw source를 확인한다.
4. 답변할 때 출처와 내 해석을 구분한다.
5. 재사용 가능한 답변은 Wiki에 다시 저장한다.
6. 파일 수정, 삭제, 대량 이동, 외부 API 사용은 승인받는다.
```

## Warnings

- Wiki에 틀린 정보가 들어가면 AI가 그 틀린 정보를 더 그럴듯하게 재생산할 수 있다.
- 출처와 내 해석이 섞이면 나중에 검증하기 어렵다.
- PDF를 대량 다운로드하면 도서관 정책 또는 저작권 문제가 생길 수 있다.
- AI 요약을 읽지 않으면 학습이 아니라 저장만 한 것이다.
- 복잡한 RAG를 만들기 전에, 작은 Wiki에서는 파일명, 태그, 링크, `rg` 검색이 먼저 중요하다.

## Practice Files

오늘 만든 LLM Wiki 설계 파일:

```text
06_LLM_Wiki\README.md
06_LLM_Wiki\Operating_Rules.md
06_LLM_Wiki\templates\Concept_Note_Template.md
06_LLM_Wiki\templates\Paper_Note_Template.md
06_LLM_Wiki\templates\Code_Note_Template.md
06_LLM_Wiki\templates\Question_Note_Template.md
06_LLM_Wiki\templates\Project_Log_Template.md
```

## LLM Wiki Note Candidate

Title: Obsidian LLM Wiki 실전 운영 원칙

Tags: `LLM Wiki`, `Obsidian`, `Agent`, `Research Workflow`, `Ingest`, `Knowledge Management`

Summary:

LLM Wiki는 단순한 자동 요약기가 아니라, 출처 원문, AI 요약, 내 해석, 질문, 작업 로그를 분리해 저장하는 개인 연구 지식 시스템이다. 일반 ingest는 자료 하나를 요약하는 과정이고, deep ingest는 기존 Wiki와 연결해 개념, 주장, 질문, 다음 reference를 확장하는 과정이다. Agent는 Wiki를 읽고 쓸 수 있지만, 파일 수정과 연구 해석에는 인간 검토와 승인 구조가 필요하다.

## Questions For Next Time

1. MCP에서 host, client, server, tool은 각각 무엇인가?
2. MCP가 LLM Wiki와 연결되면 어떤 일이 가능해지는가?
3. MCP tool을 연결할 때 어떤 보안 위험을 먼저 확인해야 하는가?
