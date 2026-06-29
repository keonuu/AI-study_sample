# Obsidian LLM Wiki 실전 운영 원칙

Tags: `LLM Wiki`, `Obsidian`, `Agent`, `Research Workflow`, `Ingest`, `Knowledge Management`

## Summary

LLM Wiki는 단순한 자동 요약기가 아니라, 출처 원문, AI 요약, 내 해석, 질문, 작업 로그를 분리해 저장하는 개인 연구 지식 시스템이다. 일반 ingest는 자료 하나를 요약하는 과정이고, deep ingest는 기존 Wiki와 연결해 개념, 주장, 질문, 다음 reference를 확장하는 과정이다. Agent는 Wiki를 읽고 쓸 수 있지만, 파일 수정과 연구 해석에는 인간 검토와 승인 구조가 필요하다.

## What Is An LLM Wiki?

LLM Wiki는 사람이 읽고 정리한 지식과 LLM이 구조화한 지식을 함께 쌓는 Markdown 기반 지식 저장소다.

좋은 LLM Wiki는 다음을 구분한다.

```text
Source: 원문, 논문, 문서, 링크, 실험 로그
AI Summary: LLM이 만든 요약과 구조화 결과
My Understanding: 사람이 검토하고 자기 언어로 다시 쓴 내용
Question: 아직 모르는 점과 다음 탐구 방향
Project Log: 실제 작업 기록과 의사결정
```

## My Understanding Rule

`My Understanding`은 AI가 대신 확정하는 영역이 아니다. AI는 후보 문장, 반론, 빠진 한계, 연결 가능한 개념을 제안할 수 있지만, 최종 문장은 사람이 읽고 검토한 뒤 자기 언어로 작성하거나 명시적으로 승인해야 한다.

따라서 LLM Wiki의 목적은 "AI가 읽은 척한 결과를 저장하는 것"이 아니라, "AI의 도움을 받아 내가 읽고 이해한 내용을 추적 가능한 형태로 저장하는 것"이다.

## Understanding Status

논문 노트와 source note에는 이해 상태를 표시한다.

```text
unread: 아직 읽지 않음
ai_skimmed: AI 요약만 받은 상태
read_basic: 사람이 요약과 핵심 내용을 읽고 확인한 상태
deep_ingested: 기존 Wiki와 연결하고 질문까지 정리한 상태
working_knowledge: 내 연구/분석에 적용할 수 있을 정도로 정리한 상태
```

`ai_skimmed`는 지식이 아니라 정리 후보에 가깝다. 이 상태의 내용을 근거로 연구 판단을 내리면 안 된다.

## General Ingest

General ingest는 자료 하나를 처음 정리하는 과정이다.

```text
bibliographic information, research question, background, method,
key result, limitation, important figure/table, short summary in my words
```

## Deep Ingest

Deep ingest는 자료 하나를 기존 Wiki와 합성하는 과정이다.

```text
related concept notes, similar claims, conflicting claims, methods comparison,
new research questions, next references to read, possible application to my project
```

## Wiki Types

### Paper Wiki

논문과 reference를 축적한다.

```text
핵심: 출처, 주장, 근거, 한계, 다음 질문
```

### Analysis Wiki

데이터 분석 프로젝트를 기록한다.

```text
핵심: 데이터 위치, preprocessing, parameter, code, result, error, decision
```

### Manuscript Wiki

원고 작성 과정을 기록한다.

```text
핵심: storyline, figure message, paragraph plan, sentence candidates, reviewer response
```

## Recommended Folder Structure

```text
My_LLM_Wiki
├── 01_raw
├── 02_wiki
│   ├── concepts
│   ├── sources
│   ├── projects
│   ├── questions
│   └── index.md
├── 03_meta
└── AGENTS.md
```

## Agent Workflow

```text
1. index를 먼저 읽는다.
2. 관련 compiled wiki note를 찾는다.
3. compiled note가 부족하면 raw source를 확인한다.
4. 출처 기반 사실과 내 해석을 구분한다.
5. 재사용 가능한 답변은 Wiki에 다시 저장한다.
6. 작업 로그를 남긴다.
```

## Search Strategy

처음부터 복잡한 RAG가 필요한 것은 아니다. 작은 Wiki에서는 좋은 파일명, frontmatter, 태그, wikilink, `rg` 검색이 먼저 중요하다. Wiki가 커지면 SQLite index, embedding, vector search, RAG, evidence map을 검토한다.

## Safety Rules

- AI 요약은 반드시 사람이 읽는다.
- `My Understanding`은 사람이 자기 언어로 쓰거나 명시적으로 승인한다.
- 핵심 연구 주장은 출처를 확인한다.
- 내 해석과 원문 주장을 섞지 않는다.
- 대량 PDF 다운로드는 도서관 정책, 저작권, 라이선스 위험을 먼저 확인한다.
- Agent가 파일을 삭제하거나 대량 수정할 때는 승인받는다.
- 비용이 발생할 수 있는 API 사용은 승인받는다.
- Wiki에 틀린 정보가 들어가면 AI 답변도 틀릴 수 있음을 기억한다.

## Bioinformatics Use Cases

- 새 연구실 또는 프로젝트 온보딩
- 공동연구자 분야와 실험 기술 이해
- 특정 분야 대가들의 논리 전개 방식 분석
- 분석 프로젝트의 parameter, code, result, error, decision 기록

## Key Takeaway

LLM Wiki의 목적은 AI에게 논문 읽기를 대신 맡기는 것이 아니다. 목적은 AI를 이용해 읽기, 질문하기, 연결하기, 자기 언어로 다시 쓰기, 연구 아이디어로 발전시키는 속도를 높이는 것이다.
