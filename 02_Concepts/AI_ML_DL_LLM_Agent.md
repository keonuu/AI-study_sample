# AI, ML, DL, LLM, Agent의 차이

Tags: `AI`, `Machine Learning`, `Deep Learning`, `LLM`, `Agent`, `Concept`

## Summary

AI는 가장 넓은 개념이고, machine learning은 데이터에서 패턴을 학습하는 AI 구현 방법 중 하나다. Deep learning은 machine learning 중 neural network를 여러 층으로 쌓아 복잡한 패턴을 학습하는 방식이다. LLM은 언어를 이해하고 생성하는 deep learning 기반 모델이며, Agent는 LLM에 도구, 작업 절차, 상태 관리, 승인 구조를 붙여 실제 작업을 수행하게 만든 시스템이다.

## Concept Map

```text
AI
└── Machine Learning
    ├── 학습 방식: 지도학습, 비지도학습, 자기지도학습, 강화학습
    └── 모델 구조: 선형 모델, tree 기반 모델, neural network 등
        └── Deep Learning
            └── LLM
```

Agent는 위 계층 안에 들어가는 단순한 모델 종류가 아니다. Agent는 LLM 같은 모델을 중심으로 도구, memory, workflow, approval, evaluation을 연결한 시스템이다.

```text
LLM = 언어를 이해하고 생성하는 두뇌
Tool = 실제 작업을 수행하는 손과 도구
Memory / Wiki = 참고할 수 있는 노트와 지식 저장소
MCP = 외부 도구와 데이터를 연결하는 표준 방식
Agent = 목표를 받고 두뇌 + 도구 + 노트를 사용해 일을 처리하는 시스템
```

## Key Distinctions

### AI

컴퓨터가 사람이 지능적으로 하는 일을 수행하게 만드는 넓은 분야다. 예를 들면 이미지 분류, 음성 인식, 데이터 분석, 논문 요약, 코드 작성 보조 등이 포함된다.

### Machine Learning

사람이 규칙을 하나하나 직접 작성하지 않고, 데이터에서 패턴을 학습하게 하는 방법이다.

Bio 예시:

- 세포 이미지에서 정상/비정상 패턴 학습
- 유전자 발현 데이터에서 cell type 분류
- 환자 metadata와 omics data를 이용한 phenotype 예측

### Deep Learning

Machine learning 중 neural network를 여러 층으로 쌓아 복잡한 패턴을 학습하는 방식이다. 이미지, sequence, language, single-cell data처럼 복잡한 데이터에서 자주 사용된다.

주의: 지도학습/비지도학습은 학습 방식이고, deep learning은 모델 구조 쪽 개념이다. Deep learning도 지도학습, 비지도학습, 자기지도학습으로 모두 사용될 수 있다.

### LLM

Large language model의 약자다. 대규모 텍스트/코드 데이터를 deep learning 방식으로 학습해 언어를 이해하고 생성한다.

할 수 있는 일:

- 질문 답변
- 요약
- 번역
- 코드 작성
- 정보 구조화
- 추론 보조
- 개념 설명

### Agent

Agent는 LLM에 목표, 도구, 작업 절차, 상태 관리, 승인/검증 구조를 붙인 시스템이다.

예시:

```text
사용자 목표: 논문 하나를 정리해줘.

Agent workflow:
1. PDF 또는 텍스트 읽기
2. 핵심 주장 추출
3. 근거 문장 확인
4. 실험 방법 요약
5. 한계점 정리
6. Obsidian 노트 작성
7. 다음 질문 생성
```

## Bioinformatics Agent Examples

1. Obsidian 노트를 주제별로 정리하고, 중복 개념을 합치고, 관련 노트끼리 링크한다.
2. NGS/RNA-seq/ChIP-seq 분석에서 QC, trimming, mapping, 정량화, peak calling 같은 pipeline을 설계하고, 승인된 명령어를 실행하며, 결과 로그를 요약한다.
3. GROMACS/MD 분석에서 입력 파일, force field, parameter, 실행 조건을 확인한 뒤, simulation 또는 후처리 pipeline을 실행하고 RMSD/RMSF/Rg 같은 결과를 정리한다.

## Safety Notes

Agent가 강력할수록 위험도 커진다.

- 파일을 잘못 수정할 수 있다.
- 비용이 발생하는 API를 호출할 수 있다.
- parameter를 잘못 설정하면 과학적으로 틀린 결과가 나올 수 있다.
- 실행은 되었지만 해석이 틀릴 수 있다.

따라서 연구/분석 Agent는 바로 실행하지 않고, 다음 순서를 따라야 한다.

1. 필요한 입력과 조건을 먼저 확인한다.
2. pipeline 계획을 제시한다.
3. 사용자 승인을 받는다.
4. 실행한다.
5. 로그와 결과를 요약한다.
6. 과학적 해석은 근거와 한계를 함께 제시한다.

## My Motivation

1. 나는 앞으로 AI가 학습, 연구, 업무 전반에 점점 더 깊게 들어올 것이라고 생각한다.
2. 그래서 앞으로의 경쟁력은 AI를 얼마나 잘 이해하고, 필요한 곳에 정확히 활용할 수 있는지에 따라 달라질 것이라고 본다.
3. 나는 대학원에서 bioinformatics와 생명과학 데이터 분석을 잘 수행하기 위해 AI를 적극적으로 활용하고 싶다.
4. 특히 NGS, RNA-seq, ChIP-seq 같은 분석 pipeline과 Python 데이터 분석 과정을 AI와 함께 자동화하고 체계화하고 싶다.
5. AI를 통해 내가 모르는 개념을 빠르게 배우고, 혼자서는 시도하기 어려웠던 분석과 연구 아이디어를 검증 가능한 방식으로 실행해보고 싶다.

## Next Questions

1. 좋은 프롬프트는 어떤 구조를 가져야 할까?
2. Codex에게 공부를 맡길 때 어디까지 믿고 어디부터 검증해야 할까?
3. 내 LLM Wiki에는 어떤 노트 템플릿이 필요할까?
