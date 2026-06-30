# Data Analysis Report Basics

## One-Line Definition

데이터 분석 리포트는 질문, 데이터, 계산, 시각화, 해석, 한계를 연결해 결과를 과장하지 않고 설명하는 문서다.

## Basic Structure

```text
analysis question
-> dataset
-> summary statistics
-> visualization
-> interpretation
-> limitation
-> next question
```

## Analysis Question

좋은 분석 질문에는 비교 대상과 측정값이 들어간다.

좋은 예:

```text
control group과 treated group 사이에서 expression 값의 평균과 분포는 어떻게 다른가?
```

약한 예:

```text
이 CSV를 분석해줘.
```

약한 이유는 무엇을 비교할지, 어떤 값을 볼지, 어디까지 해석할지 정해져 있지 않기 때문이다.

## Rows And Columns

```text
row    = 하나의 관측치 또는 sample
column = 변수, feature, group label, 측정값
```

예:

```text
sample,condition,expression
S1,control,5.0
S2,control,5.4
S3,control,5.2
S4,treated,7.2
S5,treated,8.1
S6,treated,8.1
```

```text
condition  = group label
expression = 계산할 측정값
```

## Groupby Summary

```python
summary = df.groupby("condition")["expression"].agg(["count", "mean", "std", "min", "max"])
```

뜻:

```text
condition 값이 같은 row끼리 묶고,
각 group의 expression 값에 대해 count, mean, std, min, max를 계산한다.
```

## Visualization

sample 수가 적을 때는 평균 bar plot만 보여주기보다 raw point를 같이 보여주는 것이 좋다.

```python
for condition, group_df in df.groupby("condition"):
    plt.scatter(
        [condition] * len(group_df),
        group_df["expression"],
        label=condition,
    )
```

`label=condition`은 현재 scatter 점 묶음의 이름을 group 이름으로 붙인다. `plt.legend()`를 호출하면 `control`, `treated` 같은 이름이 범례에 표시된다.

## Interpretation Discipline

좋은 해석:

```text
이 예제 데이터에서 treated group의 평균 expression은 control group보다 2.6 높게 관찰되었다.
그러나 각 group의 sample 수가 3개뿐이므로, 이 관측 결과를 treated/control group 전체의 일반적 차이로 확장하기는 어렵다.
```

피해야 할 해석:

```text
treated condition은 expression을 증가시킨다.
```

위 문장은 causality, generalization, statistical significance를 암묵적으로 주장하므로 현재 데이터만으로는 과하다.

## Key Takeaway

```text
observed difference != statistical significance
observed difference != causal effect
small n requires cautious interpretation
```
