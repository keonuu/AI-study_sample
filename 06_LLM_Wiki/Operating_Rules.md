# LLM Wiki Operating Rules

## Core Rules

1. 출처 원문, AI 요약, 내 해석을 분리한다.
2. 중요한 사실 주장에는 출처를 남긴다.
3. AI가 만든 요약은 반드시 사람이 읽고 검토한다.
4. `My Understanding`은 AI가 대신 확정하지 않는다. 사람이 자기 언어로 쓰거나 명시적으로 승인한다.
5. 이해하지 못한 내용은 그대로 지식으로 저장하지 않는다.
6. 질문과 모순은 지우지 말고 `Questions` 또는 `Contradictions / Gaps`에 남긴다.
7. Agent가 파일을 수정하기 전에는 수정 계획을 먼저 확인한다.
8. raw source는 가능한 한 수정하지 않는다.

## Ingest Levels

### General Ingest

자료 하나를 기본 정리한다.

### Deep Ingest

자료 하나를 기존 Wiki와 연결한다.

## Understanding Status

논문 노트와 source note에는 이해 상태를 표시한다.

```text
unread
ai_skimmed
read_basic
deep_ingested
working_knowledge
```

`ai_skimmed`는 AI 요약만 받은 상태이므로, 내가 이해한 지식으로 취급하지 않는다.

## Agent Approval Rules

Agent는 다음 작업 전에 승인을 받아야 한다.

```text
파일 삭제
대량 파일 이동 또는 이름 변경
외부 API 호출
비용 발생 가능 작업
raw source 수정
논문 또는 데이터 대량 다운로드
프로젝트 구조 대폭 변경
```

## Search Rules

검색 우선순위:

```text
1. 02_wiki/index.md
2. 02_wiki 안의 관련 note
3. 01_raw 원자료
4. 외부 검색 또는 새 자료
```
