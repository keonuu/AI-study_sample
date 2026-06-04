# Day 01 - AI, ML, DL, LLM, Agent의 차이

## Today's Goal

AI 관련 용어의 큰 지도를 만든다. 오늘은 코드를 많이 쓰기보다, 앞으로 30일 동안 무엇을 배우는지 이해하는 날이다.

## Key Questions

1. AI, machine learning, deep learning, LLM은 어떻게 다른가?
2. Agent는 단순한 챗봇과 무엇이 다른가?
3. 내 목표인 bioinformatics, Python 데이터 분석, LLM Wiki와 AI 흐름은 어떻게 연결되는가?

## Concept Map

- AI: 사람이 지능적으로 하는 일을 컴퓨터가 수행하게 만드는 넓은 분야.
- Machine learning: 사람이 규칙을 직접 다 쓰지 않고, 데이터에서 패턴을 학습하는 방법.
- Deep learning: neural network를 여러 층으로 쌓아 복잡한 패턴을 학습하는 machine learning의 한 분야.
- LLM: 대규모 텍스트 데이터로 학습된 언어 모델. 질문 답변, 요약, 코드 작성, 추론 보조에 사용된다.
- Agent: LLM이 목표를 이해하고, 도구를 사용하고, 중간 결과를 확인하며 여러 단계의 일을 수행하도록 만든 시스템.

## Short Example

같은 문제를 다르게 표현하면 다음과 같다.

```text
AI 질문:
컴퓨터가 이 데이터를 보고 의미 있는 결론을 내릴 수 있을까?

ML 질문:
이 데이터에서 패턴을 학습해서 새 샘플을 예측할 수 있을까?

DL 질문:
복잡한 비선형 패턴을 neural network로 학습할 수 있을까?

LLM 질문:
이 논문 내용을 요약하고, 핵심 개념을 설명하고, 분석 코드를 도와줄 수 있을까?

Agent 질문:
논문을 읽고, 근거를 추출하고, Obsidian 노트를 만들고, 관련 Python 분석까지 단계적으로 수행할 수 있을까?
```

## Main Practice

Codex와 함께 다음을 만든다.

1. 나만의 AI 용어 지도.
2. "AI를 공부하는 이유" 5문장.
3. LLM Wiki에 넣을 첫 번째 개념 노트 초안.

## My Understanding After Study

### LLM vs Agent

LLM은 large language model의 약자이며, 대규모 텍스트/코드 데이터를 deep learning 방식으로 학습한 언어 모델이다. 질문에 답하는 것은 LLM의 대표적인 사용 방식이지만, LLM의 본질은 주어진 문맥을 바탕으로 언어를 이해하고 생성하는 데 있다.

Agent는 LLM에 목표, 도구, 작업 절차, 상태 관리, 승인/검증 구조를 붙여 실제 작업을 수행하게 만든 시스템이다. LLM이 주로 답변을 생성한다면, Agent는 파일 읽기, 검색, 코드 실행, 노트 작성, 분석 pipeline 실행 보조 같은 행동까지 수행할 수 있다.

중요한 점은 Agent가 강력할수록 위험도 커진다는 것이다. 연구/분석 작업에서는 입력 조건, 실행 환경, parameter, 검증 기준, 사용자 승인 구조가 반드시 필요하다.

### AI, Machine Learning, Deep Learning

AI는 가장 넓은 분야이고, machine learning은 AI를 구현하는 대표적인 방법 중 하나다. Deep learning은 machine learning 중에서도 neural network를 여러 층으로 쌓아 복잡한 패턴을 학습하는 방식이다.

주의할 점은 지도학습/비지도학습과 deep learning은 같은 분류 축이 아니라는 것이다. 지도학습과 비지도학습은 "어떻게 배우는가"에 대한 분류이고, deep learning은 "어떤 모델 구조를 쓰는가"에 대한 분류다.

```text
AI
└── Machine Learning
    ├── 학습 방식: 지도학습, 비지도학습, 자기지도학습, 강화학습
    └── 모델 구조: 선형 모델, tree 기반 모델, neural network 등
        └── Deep Learning: 깊은 neural network를 쓰는 방식
```

### Agent Use Cases For My Bioinformatics Goals

1. Obsidian 노트를 주제별로 정리하고, 중복 개념을 합치고, 관련 노트끼리 링크해준다.
2. NGS/RNA-seq/ChIP-seq 분석에서 QC, trimming, mapping, 정량화, peak calling 같은 pipeline을 설계하고, 승인된 명령어를 실행하며, 결과 로그를 요약해준다.
3. GROMACS/MD 분석에서 입력 파일, force field, parameter, 실행 조건을 확인한 뒤, simulation 또는 후처리 pipeline을 실행하고 RMSD/RMSF/Rg 같은 결과를 정리해준다.

다만 bioinformatics pipeline이나 MD simulation은 실행 자체보다 parameter 선택과 결과 해석이 중요하다. AI가 도와줄 수는 있지만, 과학적 검증 책임은 연구자에게 남아 있다.

## Why I Study AI

1. 나는 앞으로 AI가 학습, 연구, 업무 전반에 점점 더 깊게 들어올 것이라고 생각한다.
2. 그래서 앞으로의 경쟁력은 AI를 얼마나 잘 이해하고, 필요한 곳에 정확히 활용할 수 있는지에 따라 달라질 것이라고 본다.
3. 나는 대학원에서 bioinformatics와 생명과학 데이터 분석을 잘 수행하기 위해 AI를 적극적으로 활용하고 싶다.
4. 특히 NGS, RNA-seq, ChIP-seq 같은 분석 pipeline과 Python 데이터 분석 과정을 AI와 함께 자동화하고 체계화하고 싶다.
5. AI를 통해 내가 모르는 개념을 빠르게 배우고, 혼자서는 시도하기 어려웠던 분석과 연구 아이디어를 검증 가능한 방식으로 실행해보고 싶다.

## LLM Wiki Note Candidate

Title: AI, ML, DL, LLM, Agent의 차이

Tags: `AI`, `Machine Learning`, `Deep Learning`, `LLM`, `Agent`, `Concept`

Summary:

AI는 가장 넓은 개념이고, machine learning은 데이터에서 패턴을 학습하는 방식이며, deep learning은 neural network 기반의 machine learning이다. LLM은 언어를 다루는 대규모 모델이고, Agent는 LLM이 도구와 절차를 사용해 여러 단계의 작업을 수행하도록 만든 시스템이다.

## Questions For Next Time

1. 좋은 프롬프트는 어떤 구조를 가져야 할까?
2. Codex에게 공부를 맡길 때 어디까지 믿고 어디부터 검증해야 할까?
3. 내 LLM Wiki에는 어떤 노트 템플릿이 필요할까?
