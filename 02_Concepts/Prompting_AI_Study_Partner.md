# Codex/ChatGPT를 학습 파트너로 쓰는 법

Tags: `Prompting`, `Codex`, `ChatGPT`, `Learning`, `LLM Wiki`

## Summary

AI를 잘 쓰려면 질문을 많이 하는 것보다 문제를 정확히 정의해야 한다. 좋은 질문은 목표, 현재 상태, 입력 자료, 원하는 출력, 제약 조건, 검증 기준을 포함한다. AI 답변은 최종 정답이 아니라 초안으로 보고, 출처와 가정, 불확실성, 실행 전 확인 조건을 검증해야 한다.

## Good Prompt Structure

```text
내 목표는 [목표]이다.

내 현재 수준은 [현재 상태]이다.

현재 가지고 있는 자료/상황은 [입력 자료]이다.

원하는 출력은 [원하는 결과물]이다.

제약 조건은 [제약 조건]이다.

답변할 때 [검증 기준]을 포함해줘.
내 논리나 계획에 문제가 있으면 지적해줘.
```

## Why This Matters

AI는 사용자의 질문에 들어 있는 정보만 보고 답변 방향을 잡는다. 질문이 모호하면 AI는 빈칸을 추측으로 채우기 쉽다. 특히 bioinformatics, 논문 해석, 분석 pipeline처럼 정확성이 중요한 작업에서는 목표와 입력 자료, 제약 조건, 검증 기준을 분명히 해야 한다.

## Verification Questions

```text
이 답변에서 불확실한 부분은 무엇이야?
어떤 가정에 의존하고 있어?
출처가 필요한 주장은 무엇이야?
내가 초보자라서 놓칠 수 있는 위험은 뭐야?
실제로 실행하기 전에 확인해야 할 조건은 뭐야?
```

## LLM Wiki Prompt Example

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

## Notes

- 링크나 문서를 첨부했을 때는 "이 자료에 기반해서 답변하라"고 명시한다.
- 문서에 없는 내용을 제안할 때는 "추가 제안"으로 구분하게 한다.
- 필요한 정보가 부족하면 AI가 추측하지 말고 질문하게 만든다.

