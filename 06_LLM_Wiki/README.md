# LLM Wiki Design Draft

이 폴더는 실제 Obsidian vault가 아니라, 앞으로 만들 Obsidian LLM Wiki의 설계 초안이다.

## Goal

```text
1. 공부한 개념을 다시 찾을 수 있게 저장한다.
2. 논문과 출처를 근거 기반으로 정리한다.
3. Python/ML/bioinformatics 실습을 코드와 함께 기록한다.
4. Agent가 읽고 활용할 수 있는 구조로 만든다.
5. 틀린 정보와 근거 부족한 주장을 나중에 고칠 수 있게 한다.
```

## Recommended Vault Structure

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

## Start Small

처음에는 다음 4종류만 시작한다.

```text
Concept note
Paper note
Code note
Question note
```

이후 실제 연구 프로젝트가 생기면 `Project note`와 `Analysis log`를 추가한다.
