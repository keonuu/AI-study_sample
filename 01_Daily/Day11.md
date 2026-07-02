# Day 11 - 재현 가능한 데이터 분석 프로젝트 구조

## Today's Goal

raw, processed, results, notebooks 구조를 이해하고 분석 프로젝트의 기본 틀을 만든다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 11을 따른다.

## Review From Day 8-10

- Day 8: LLM Wiki는 `Source`, `AI Summary`, `My Understanding`을 분리해서 관리하는 개인 지식 시스템이다.
- Day 9: MCP는 LLM host app이 외부 tools, resources, prompts를 표준 방식으로 사용할 수 있게 하는 구조이며, 연결 전 권한과 보안 범위를 확인해야 한다.
- Day 10: 작은 데이터 분석은 `분석 질문 -> 데이터 -> 요약 통계 -> 시각화 -> 해석 -> 한계` 흐름으로 진행하며, observed difference와 statistical significance를 구분해야 한다.

## Work Log

- 재현 가능한 데이터 분석 프로젝트에서는 raw data를 분석 중 직접 수정하지 않고, 원본으로 보존해야 함을 배웠다.
- `raw`, `processed`, `results`, `notebooks`, `scripts`의 역할을 구분했다.
- `notebooks/`는 탐색, 비교, 시행착오를 위한 공간이고, `scripts/`는 같은 입력에서 같은 결과를 반복 생성하는 재현 가능한 코드 공간임을 확인했다.
- `raw -> script -> processed -> script -> results` 흐름을 기준으로 생각해야 함을 정리했다.
- 분석 결과를 재현하려면 최소한 `input`, `code`, `output`이 연결되어 있어야 함을 배웠다.
- README에는 raw data 위치와 script 실행 순서가 포함되어야 함을 확인했다.
- Day 10 expression 예제를 Day 11 방식의 작은 연습 프로젝트로 구성하고, script 실행으로 processed CSV와 figure PNG를 생성했다.

## Core Idea

재현 가능한 데이터 분석은 결과 파일을 한 번 만드는 것이 아니라, 같은 raw data와 같은 script로 같은 output을 다시 만들 수 있게 하는 것이다.

```text
input  = raw data
code   = script
output = processed data / results
```

더 구체적인 흐름은 다음과 같다.

```text
data/raw/expression_samples.csv
  -> scripts/run_expression_pipeline.py
    -> data/processed/expression_summary.csv
    -> results/figures/expression_raw_points.png
```

## Folder Role Summary

```text
data/raw/        원본 데이터, 분석 중 직접 수정하지 않음
data/processed/  raw data에서 script로 생성한 중간 산출물
results/         분석 결과 표, 그림, 리포트
notebooks/       탐색, 비교, 시행착오용 분석 노트
scripts/         재실행 가능한 분석 코드
README.md        실행 순서와 output 위치 설명
```

## Correction Points

> [!CAUTION]
> [오답/교정] group별 summary CSV는 raw data가 아니라 `data/processed/` 또는 `results/tables/`에 두는 것이 더 적절하다. raw data는 처음 받은 원본만 의미한다.

> [!CAUTION]
> [오답/교정] `make_summary.py`와 `plot_expression.py`는 둘 다 정해진 입력에서 정해진 결과를 반복 생성하는 코드이므로 `scripts/`에 더 적절하다. `notebooks/` 여부는 파일명이 아니라 탐색용인지 재실행용인지로 판단한다.

> [!CAUTION]
> [오답/교정] `processed`를 수정하고 싶을 때는 processed 파일을 손으로 직접 고치는 것이 아니라, script를 수정하고 processed를 다시 생성하는 것이 더 재현 가능하다.

> [!CAUTION]
> [오답/교정] `raw, script, result`라는 3묶음은 좋은 출발점이지만, 더 정확히는 `raw, script, processed/results`로 이해해야 한다. processed도 중요한 output이다.

## Practice Project

오늘 만든 연습 프로젝트:

```text
04_Data_Analysis/day11_reproducible_project/
  README.md
  data/raw/expression_samples.csv
  data/processed/expression_summary.csv
  notebooks/README.md
  results/figures/expression_raw_points.png
  scripts/run_expression_pipeline.py
```

실행 명령:

```powershell
python scripts\run_expression_pipeline.py
```

생성된 summary:

```text
condition,count,mean,std,min,max
control,3,5.2,0.20000000000000018,5.0,5.4
treated,3,7.8,0.5196152422706626,7.2,8.1
```

## LLM Wiki Note Candidate

Title: 재현 가능한 데이터 분석 프로젝트 구조

Tags: `data analysis`, `reproducibility`, `raw data`, `processed data`, `scripts`, `results`

Summary:

재현 가능한 데이터 분석 프로젝트에서는 raw data를 직접 수정하지 않고, script를 통해 processed data와 results를 생성한다. `notebooks/`는 탐색과 시행착오에 적합하고, `scripts/`는 반복 실행 가능한 분석 흐름을 저장하는 데 적합하다. 좋은 분석 기록은 input(raw data), code(script), output(processed/results)을 연결해서 나중에 같은 결과를 다시 만들 수 있게 한다.

## Questions For Next Time

1. Day 12에서 Git branch를 만들 때, 왜 main/master에서 바로 작업하지 않고 branch를 나누는가?
2. 재현 가능한 분석 프로젝트에서 commit message는 어떤 단위로 나누는 것이 좋은가?
3. GitHub pull request는 단순 업로드가 아니라 어떤 검토 흐름을 만들기 위한 도구인가?