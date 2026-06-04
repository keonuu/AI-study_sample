# Day 02 - Codex/ChatGPT를 학습 파트너로 쓰는 법

## Today's Goal

좋은 질문 구조를 배우고, AI 답변을 검증하며, Codex를 학습 파트너로 쓰는 기본 루틴을 만든다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 2를 따른다.

## Work Log

- 좋은 질문은 단순한 질문이 아니라 작업 지시서에 가깝다는 점을 배웠다.
- 좋은 질문에는 목표, 현재 상태, 입력 자료, 원하는 출력, 제약 조건, 검증 기준이 들어가야 한다.
- AI 답변은 최종 정답이 아니라 초안으로 보고, 특히 학술/연구/분석 내용은 검증해야 한다.
- Codex는 설명만 하는 도구가 아니라 프로젝트 폴더의 파일을 읽고 수정하고 명령어를 실행할 수 있으므로, 작업 전 계획과 승인 구조가 중요하다.

## Core Template

```text
내 목표는 [목표]이다.

내 현재 수준은 [현재 상태]이다.

현재 가지고 있는 자료/상황은 [입력 자료]이다.

원하는 출력은 [원하는 결과물]이다.

제약 조건은 [제약 조건]이다.

답변할 때 [검증 기준]을 포함해줘.
내 논리나 계획에 문제가 있으면 지적해줘.
```

## Bad Prompt vs Good Prompt

나쁜 질문:

```text
NGS 분석 어떻게 해?
```

좋은 질문:

```text
나는 Python과 bioinformatics를 배우는 초보자다.
목표는 RNA-seq raw FASTQ 파일에서 gene expression count matrix를 만드는 전체 흐름을 이해하는 것이다.
아직 직접 실행하지는 말고, 먼저 단계별 pipeline을 설명해줘.
각 단계에서 사용하는 대표 도구와 입력/출력 파일을 표로 정리해줘.
학술적으로 중요한 부분은 근거가 필요하면 출처도 함께 알려줘.
```

## Verification Questions

AI 답변을 검증하기 위해 다음 질문을 붙일 수 있다.

```text
이 답변에서 불확실한 부분은 무엇이야?
어떤 가정에 의존하고 있어?
출처가 필요한 주장은 무엇이야?
내가 초보자라서 놓칠 수 있는 위험은 뭐야?
실제로 실행하기 전에 확인해야 할 조건은 뭐야?
```

## LLM Wiki Prompt Practice

오늘 연습 주제는 Andrej Karpathy의 LLM Wiki 설명을 참고해 개인 LLM Wiki를 만드는 질문을 작성하는 것이었다.

참고 링크:

```text
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
```

개선된 질문:

```text
나는 Windows 노트북에서 Obsidian을 사용하고 있고, 개인용 LLM Wiki를 만들고 싶다.

내 현재 수준:
- LLM Wiki라는 단어만 들어봤다.
- Andrej Karpathy가 말한 LLM Wiki의 핵심 개념, 구성 방식, 운영 방식은 아직 잘 모른다.
- Git/GitHub, MCP, Obsidian 고급 기능도 초보자 수준이다.

참고해야 할 1차 자료:
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

요청:
1. 위 링크의 내용을 근거로 Karpathy식 LLM Wiki의 핵심 아이디어를 쉽게 설명해줘.
2. 단순 RAG와 LLM Wiki가 어떻게 다른지 설명해줘.
3. Windows + Obsidian 환경에서 내가 만들 수 있는 폴더 구조를 제안해줘.
4. raw sources, wiki, schema, index.md, log.md가 각각 무슨 역할인지 설명해줘.
5. 내가 bioinformatics, 머신러닝/딥러닝, Python 데이터 분석 공부에 쓸 수 있도록 구조를 맞춰줘.
6. 실제 폴더나 파일을 만들기 전에 필요한 정보가 있으면 추측하지 말고 먼저 질문해줘.
7. 답변은 첨부한 Karpathy gist에 기반해서 하고, gist에 없는 내용은 명확히 "추가 제안"이라고 구분해줘.
8. 내가 초보자이므로 개발 용어는 쉽게 설명해줘.
```

## Clarifying Questions For LLM Wiki Setup

실제 LLM Wiki를 만들기 전에 확인해야 할 질문:

1. Obsidian vault 위치는 어디인가?
2. 새 vault로 만들 것인가, 기존 vault 안에 만들 것인가?
3. 처음 넣을 source는 무엇인가?
4. Git 버전 관리는 Day 4 이후 시작할 것인가, 지금 바로 시작할 것인가?

## LLM Wiki Note Candidate

Title: Codex/ChatGPT를 학습 파트너로 쓰는 법

Tags: `Prompting`, `Codex`, `ChatGPT`, `Learning`, `LLM Wiki`

Summary:

AI를 잘 쓰려면 질문을 많이 하는 것보다 문제를 정확히 정의해야 한다. 좋은 질문에는 목표, 현재 상태, 입력 자료, 원하는 출력, 제약 조건, 검증 기준이 들어간다. AI 답변은 초안으로 보고, 출처와 가정, 불확실성, 실행 전 확인 조건을 점검해야 한다.

## Questions For Next Time

1. 파일 경로와 현재 작업 위치는 왜 중요한가?
2. PowerShell에서 현재 위치를 확인하고 이동하는 명령어는 무엇인가?
3. Windows 경로와 Ubuntu/WSL 경로는 어떻게 다른가?
