# Day 07 - pandas/numpy/matplotlib 기초

## Today's Goal

표 데이터, 숫자 배열, 그래프의 역할을 이해하고 작은 데이터를 시각화한다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 7을 따른다.

## Work Log

- Day 1의 AI/ML/DL/LLM/Agent 개념을 복습했다.
- `if`, `for` 자체는 일반 프로그래밍 문법이며, 요즘 ML 맥락의 AI와는 구분해야 함을 정리했다.
- AI는 가장 넓은 분야, ML은 데이터에서 패턴을 학습하는 방식, DL은 neural network 기반 모델 구조임을 복습했다.
- 지도학습/비지도학습은 모델 구조가 아니라 학습 방식이라는 점을 다시 확인했다.
- pandas는 표 데이터, numpy는 숫자 배열과 계산, matplotlib은 그래프를 다루는 도구로 구분했다.
- pandas의 `DataFrame`을 Python 안의 엑셀 표처럼 이해했다.
- dictionary의 key가 DataFrame의 column 이름이 되고, value list가 column 값이 됨을 배웠다.
- `df["column_name"]`으로 특정 column을 꺼내는 방법을 배웠다.
- `.mean()`, `.max()`, `.min()`으로 숫자 column의 요약 통계를 계산했다.
- `df[df["mapping_rate"] >= 0.8]`처럼 조건을 이용해 행을 필터링하는 방법을 배웠다.
- 현재 Python 환경에서 `pandas`, `numpy`, `matplotlib`이 모두 import 가능함을 확인했다.
- 작은 CSV 파일을 만들고, pandas로 읽고, QC 결과 column을 만들고, 그래프를 저장하는 실습 파일을 작성했다.

## Environment Check

다음 명령어로 패키지 설치 여부를 확인했다.

```powershell
py -c "import pandas, numpy, matplotlib; print('pandas/numpy/matplotlib import ok')"
```

확인 결과:

```text
pandas/numpy/matplotlib import ok
```

## Concepts Learned

### pandas

pandas는 표 데이터를 다루는 도구다. Python 안의 엑셀 표처럼 생각할 수 있다.

```python
import pandas as pd

data = {
    "sample_id": ["S01", "S02", "S03"],
    "mapping_rate": [0.92, 0.76, 0.84],
}

df = pd.DataFrame(data)
```

### DataFrame

DataFrame은 행과 열을 가진 표 형태의 데이터다.

```text
sample_id | mapping_rate
S01       | 0.92
S02       | 0.76
S03       | 0.84
```

이 예시에서:

```text
row = sample 하나
column = sample에 대해 기록한 정보 종류
```

### Column Selection

특정 열은 다음처럼 꺼낸다.

```python
df["mapping_rate"]
```

### Summary Statistics

숫자 column에는 평균, 최댓값, 최솟값을 바로 계산할 수 있다.

```python
print(df["mapping_rate"].mean())
print(df["mapping_rate"].max())
print(df["mapping_rate"].min())
```

### Filtering Rows

조건에 맞는 행만 남길 수 있다.

```python
passed = df[df["mapping_rate"] >= 0.8]
failed = df[df["mapping_rate"] < 0.8]
```

핵심 구조:

```text
조건 만들기 -> True인 행만 남기기
```

### matplotlib

matplotlib은 그래프를 그리는 도구다. 오늘은 sample별 mapping rate를 bar plot으로 저장했다.

## Practice Files

오늘 만든 예제 CSV:

```text
04_Data_Analysis\day07_sample_qc.csv
```

오늘 만든 Python 실습 파일:

```text
03_Python_Practice\day07_pandas_numpy_matplotlib.py
```

실행 명령어:

```powershell
py 03_Python_Practice\day07_pandas_numpy_matplotlib.py
```

실행 결과 생성되는 그래프:

```text
04_Data_Analysis\day07_mapping_rate_barplot.png
```

## Practice Difficulty

### Basic

`df["condition"]`은 어떤 정보를 꺼내는가?

### Intermediate

`mapping_rate >= 0.8`인 sample만 남기면 어떤 sample이 남는가?

### Advanced

`mapping_rate` 기준으로 `"excellent"`, `"pass"`, `"fail"`을 나누는 QC 결과 column을 직접 만들 수 있는가?

## LLM Wiki Note Candidate

Title: pandas, numpy, matplotlib 기초

Tags: `Python`, `pandas`, `numpy`, `matplotlib`, `DataFrame`, `Data Analysis`

Summary:

pandas는 표 데이터를 다루는 도구이고, numpy는 숫자 배열과 계산을 다루며, matplotlib은 그래프를 그리는 도구다. pandas의 DataFrame은 행과 열을 가진 표 형태의 데이터이며, `df["column_name"]`으로 특정 열을 꺼내고, 조건식을 이용해 원하는 행만 필터링할 수 있다.

## Questions For Next Time

1. Obsidian LLM Wiki에서 concept note, paper note, code note는 어떻게 나누는가?
2. 오늘 만든 pandas 실습 결과를 LLM Wiki에 어떤 형태로 저장하면 좋은가?
3. 데이터 분석 코드와 개념 노트를 서로 연결하려면 어떤 링크 구조가 필요한가?
