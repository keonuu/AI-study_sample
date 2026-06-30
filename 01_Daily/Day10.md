# Day 10 - 초보 미니 프로젝트

## Today's Goal

작은 데이터셋을 불러오고 요약한 뒤, 분석 리포트와 Wiki 노트를 만든다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 10을 따른다.

## Review From Day 09

- MCP는 LLM 앱이 외부 tools, resources, prompts를 표준 방식으로 발견하고 사용할 수 있게 하는 구조다.
- Host는 사용자가 쓰는 AI 앱, client는 server별 연결 담당자, server는 외부 도구와 데이터를 제공하는 프로그램이다.
- MCP 연결 전에는 파일 읽기/쓰기 범위, 네트워크 권한, 비용 발생 가능성, 자동 승인 여부를 먼저 점검해야 한다.

## Analysis Question

control group과 treated group 사이에서 expression 값의 평균과 분포는 어떻게 다른가?

## Example Dataset

```text
sample,condition,expression
S1,control,5.0
S2,control,5.4
S3,control,5.2
S4,treated,7.2
S5,treated,8.1
S6,treated,8.1
```

## Work Log

- 데이터 분석은 먼저 분석 질문을 정한 뒤 진행해야 함을 확인했다. `이 CSV를 분석해줘`보다 `group별 평균 측정값이 서로 다른지 확인하고 싶다`가 더 좋은 질문이다.
- DataFrame에서 row는 하나의 관측치 또는 sample이고, column은 변수 또는 측정 항목임을 복습했다.
- `df.groupby("condition")["expression"].agg(["count", "mean", "std", "min", "max"])`의 의미를 해석했다.
  - `condition`: row들을 group으로 나누는 기준
  - `expression`: 실제 계산 대상인 측정값
  - `agg`: group별 count, mean, std, min, max 계산
- 평균만 보면 분포 차이를 놓칠 수 있으므로 std, min, max, raw point를 함께 봐야 함을 확인했다.
- sample 수가 적을 때 평균 bar plot만 보여주면 개별 sample 값과 분포를 숨길 수 있으므로 raw point plot이 더 정직하다는 점을 배웠다.
- `label=condition`은 scatter plot에서 현재 group의 이름을 legend에 표시하기 위한 label임을 확인했다.

## Summary Result

```text
condition  count  mean       std  min  max
control        3   5.2  0.200000  5.0  5.4
treated        3   7.8  0.519615  7.2  8.1
```

## Interpretation

이 예제 데이터에서 treated group의 평균 expression은 control group보다 2.6 높게 관찰되었다.
그러나 각 group의 sample 수가 3개뿐이므로, 이 관측 결과를 treated/control group 전체의 일반적 차이로 확장하기는 어렵다.
따라서 더 많은 sample을 포함한 추가 분석이 필요하다.

## Correction Points

- `유의하다`는 표현은 통계적 검정을 거친 뒤에만 조심해서 사용해야 한다.
- 지금 결과는 `observed difference`이지, `statistical significance`나 `causal effect`가 아니다.
- `condition`은 분석 대상 자체가 아니라 group label이고, 실제 계산 대상은 `expression`이다.
- n=3처럼 sample 수가 작을 때 boxplot이나 bar plot만 보면 과해석할 수 있으므로 raw data point를 같이 보는 것이 좋다.

## Files Updated Today

```text
01_Daily/Day10.md
02_Concepts/Data_Analysis_Report_Basics.md
03_Python_Practice/day10_expression_summary.py
04_Data_Analysis/day10_expression_summary.csv
04_Data_Analysis/day10_expression_raw_points.png
```

## LLM Wiki Note Candidate

Title: 데이터 분석 리포트의 기본 구조

Tags: `data analysis`, `pandas`, `groupby`, `visualization`, `interpretation`, `limitation`

Summary:

작은 데이터 분석 리포트는 `분석 질문 -> 데이터 -> 계산 -> 시각화 -> 해석 -> 한계` 구조를 가져야 한다. 분석 질문에는 비교 대상과 측정값이 들어가야 한다. pandas에서는 `groupby`로 group label에 따라 row를 나누고, 측정값 column에 대해 count, mean, std, min, max 같은 요약 통계를 계산할 수 있다. 결과 해석에서는 관찰된 차이와 통계적 유의성, 인과효과, 일반화 가능성을 구분해야 한다.

## Questions For Next Time

1. sample 수가 더 많아지면 group별 차이를 어떤 통계 검정으로 확인할 수 있을까?
2. 평균, 표준편차, raw point plot 외에 데이터 분포를 확인하는 방법은 무엇이 있을까?
3. Day 11에서 raw/processed/results 구조를 만들 때 오늘의 CSV와 plot은 어느 폴더에 두는 것이 적절할까?
