# pandas, numpy, matplotlib 기초

Tags: `Python`, `pandas`, `numpy`, `matplotlib`, `DataFrame`, `Data Analysis`

## Summary

pandas는 표 데이터를 다루는 도구이고, numpy는 숫자 배열과 계산을 다루며, matplotlib은 그래프를 그리는 도구다. pandas의 DataFrame은 행과 열을 가진 표 형태의 데이터이며, `df["column_name"]`으로 특정 열을 꺼내고, 조건식을 이용해 원하는 행만 필터링할 수 있다.

## Three Tools

### pandas

pandas는 표 데이터를 다룬다.

```text
CSV 파일
Excel 형태의 표
sample metadata
gene expression matrix
QC summary table
```

핵심 객체는 `DataFrame`이다.

### numpy

numpy는 숫자 배열과 계산을 다룬다.

```text
평균
표준편차
숫자 배열
행렬 계산
```

pandas 내부에서도 숫자 계산에 numpy가 자주 사용된다.

### matplotlib

matplotlib은 그래프를 그린다.

```text
bar plot
line plot
scatter plot
histogram
```

## DataFrame

DataFrame은 Python 안의 엑셀 표처럼 생각할 수 있다.

```python
import pandas as pd

data = {
    "sample_id": ["S01", "S02", "S03"],
    "condition": ["control", "treated", "treated"],
    "mapping_rate": [0.92, 0.76, 0.84],
}

df = pd.DataFrame(data)
print(df)
```

표로 보면:

```text
sample_id | condition | mapping_rate
S01       | control   | 0.92
S02       | treated   | 0.76
S03       | treated   | 0.84
```

## Row And Column

행은 관측 단위다.

```text
S01 행
S02 행
S03 행
```

열은 각 관측 단위에 대해 기록한 정보 종류다.

```text
sample_id 열
condition 열
mapping_rate 열
```

bioinformatics에서는 데이터 형태에 따라 행이 sample일 수도 있고, gene이나 cell일 수도 있다. 그래서 표를 처음 볼 때는 항상 다음 질문을 해야 한다.

```text
이 표에서 한 행은 무엇을 의미하는가?
이 표에서 한 열은 무엇을 의미하는가?
```

## Selecting A Column

특정 열은 다음처럼 꺼낸다.

```python
print(df["condition"])
```

의미:

```text
df에서 condition 열을 꺼낸다.
```

숫자 열도 같은 방식으로 꺼낸다.

```python
print(df["mapping_rate"])
```

## Summary Statistics

숫자 column에는 평균, 최댓값, 최솟값을 계산할 수 있다.

```python
print(df["mapping_rate"].mean())
print(df["mapping_rate"].max())
print(df["mapping_rate"].min())
```

예시 값:

```text
mean: 0.84
max: 0.92
min: 0.76
```

## Filtering Rows

조건에 맞는 행만 남길 수 있다.

```python
passed = df[df["mapping_rate"] >= 0.8]
```

이 코드는 두 단계로 이해한다.

```text
1. df["mapping_rate"] >= 0.8 조건으로 True/False 목록을 만든다.
2. df[...] 안에 그 조건을 넣어 True인 행만 남긴다.
```

예:

```text
S01: 0.92 >= 0.8 -> True
S02: 0.76 >= 0.8 -> False
S03: 0.84 >= 0.8 -> True
```

따라서 S01, S03만 남는다.

## Creating A New Column

기존 column을 바탕으로 새 column을 만들 수 있다.

```python
def check_qc(rate):
    if rate >= 0.9:
        return "excellent"
    elif rate >= 0.8:
        return "pass"
    else:
        return "fail"

df["qc_result"] = df["mapping_rate"].apply(check_qc)
```

의미:

```text
mapping_rate 열의 각 값에 check_qc 함수를 적용한다.
그 결과를 qc_result라는 새 열에 저장한다.
```

## Saving A Plot

matplotlib으로 그래프를 저장할 수 있다.

```python
import matplotlib.pyplot as plt

plt.bar(df["sample_id"], df["mapping_rate"])
plt.axhline(0.8, color="red", linestyle="--")
plt.savefig("04_Data_Analysis/day07_mapping_rate_barplot.png")
```

`plt.axhline(0.8)`은 y축 값 0.8 위치에 기준선을 그린다.

## Key Takeaway

```text
pandas = 표 데이터 읽기, 정리, 필터링
numpy = 숫자 계산
matplotlib = 그래프 그리기
```

Day 7의 핵심은 머신러닝 전에 데이터를 눈으로 확인하고, 요약하고, 이상한 sample을 찾는 기초 흐름을 만드는 것이다.
