# Day 06 - Python 기초 2: 조건문, 반복문, 함수

## Today's Goal

조건문, 반복문, 함수를 이해하고 작은 QC 판단 프로그램을 만든다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 6을 따른다.

## Work Log

- `if`, `elif`, `else`를 사용해 조건에 따라 다른 코드를 실행하는 방법을 배웠다.
- 비교 연산자 `>=`, `>`, `<=`, `<`, `==`, `!=`의 의미를 확인했다.
- Python에서는 들여쓰기가 코드의 소속을 결정한다는 점을 배웠다.
- `if / elif / else`는 위에서부터 조건을 검사하고, 처음 맞는 조건 하나만 실행한다.
- 더 엄격한 조건을 위에 두어야 원하는 분류 결과가 나온다는 점을 확인했다.
- `for` 반복문으로 list 안의 값을 하나씩 꺼내 처리하는 방법을 배웠다.
- `def`로 함수를 만들고, `return`으로 함수 결과를 밖으로 돌려주는 방법을 배웠다.
- `print()`는 화면에 보여주는 것이고, `return`은 함수의 결과를 돌려주는 것임을 구분했다.
- `list` 안에 `dict`를 넣어 여러 sample의 `sample_id`와 `mapping_rate`를 함께 다루는 예제를 연습했다.

## Concepts Learned

### Conditional Statement

조건문은 조건에 따라 다른 코드를 실행하게 한다.

```python
mapping_rate = 0.76

if mapping_rate >= 0.8:
    print("pass")
else:
    print("fail")
```

출력:

```text
fail
```

### if / elif / else Order

`if / elif / else`는 위에서부터 조건을 검사하고, 처음으로 맞는 조건 하나만 실행한다.

```python
def check_qc(rate):
    if rate >= 0.9:
        return "excellent"
    elif rate >= 0.8:
        return "pass"
    else:
        return "fail"
```

`0.92`는 `0.9` 이상이므로 `"excellent"`가 된다.

반대로 아래 코드는 논리적으로 문제가 있다.

```python
def check_qc(rate):
    if rate >= 0.8:
        return "pass"
    elif rate >= 0.9:
        return "excellent"
    else:
        return "fail"
```

이 경우 `0.92`도 첫 번째 조건 `rate >= 0.8`에서 이미 걸리기 때문에 `"excellent"`가 나올 수 없다.

### For Loop

반복문은 list 안의 값을 하나씩 꺼내 같은 작업을 반복한다.

```python
samples = ["S01", "S02", "S03"]

for sample in samples:
    print(sample)
```

출력:

```text
S01
S02
S03
```

### Function

함수는 자주 쓰는 판단이나 계산을 이름 붙여 저장한 코드 묶음이다.

```python
def check_qc(rate):
    if rate >= 0.8:
        return "pass"
    else:
        return "fail"
```

사용 예:

```python
result = check_qc(0.76)
print(result)
```

출력:

```text
fail
```

## Bioinformatics-Style Example

```python
def check_qc(rate):
    if rate >= 0.9:
        return "excellent"
    elif rate >= 0.8:
        return "pass"
    else:
        return "fail"

samples = [
    {"sample_id": "S01", "mapping_rate": 0.92},
    {"sample_id": "S02", "mapping_rate": 0.76},
    {"sample_id": "S03", "mapping_rate": 0.84},
]

for sample in samples:
    result = check_qc(sample["mapping_rate"])
    print(sample["sample_id"], result)
```

출력:

```text
S01 excellent
S02 fail
S03 pass
```

## Practice File

오늘 만든 Python 실습 파일:

```text
03_Python_Practice\day06_control_flow.py
```

실행 명령어:

```powershell
py 03_Python_Practice\day06_control_flow.py
```

## Common Mistakes

### Confusing print And return

```python
return "pass"
```

함수의 결과를 밖으로 돌려준다.

```python
print(result)
```

값을 화면에 보여준다.

### Wrong Condition Order

좁은 조건을 아래에 두면 실행되지 않을 수 있다.

```python
if rate >= 0.8:
    return "pass"
elif rate >= 0.9:
    return "excellent"
```

`0.9` 이상인 값도 첫 번째 조건에서 이미 `"pass"`가 되므로 `"excellent"`는 나오지 않는다.

### Indentation

Python에서는 들여쓰기가 중요하다. 들여쓰기가 달라지면 코드가 어느 조건문, 반복문, 함수에 속하는지도 달라진다.

## LLM Wiki Note Candidate

Title: Python 조건문, 반복문, 함수

Tags: `Python`, `Conditional`, `Loop`, `Function`, `QC`, `Beginner`

Summary:

Python에서 조건문은 조건에 따라 다른 코드를 실행하고, 반복문은 여러 값을 하나씩 처리하며, 함수는 자주 쓰는 판단이나 계산을 이름 붙여 재사용하게 한다. `if / elif / else`는 위에서부터 조건을 검사해 처음 맞는 조건 하나만 실행하므로 조건의 순서가 중요하다. `return`은 함수의 결과를 밖으로 돌려주는 것이고, `print()`는 값을 화면에 보여주는 것이다.

## Questions For Next Time

1. Python에서 데이터를 표 형태로 다루려면 어떤 도구가 필요한가?
2. pandas의 DataFrame은 list와 dictionary와 어떻게 연결되는가?
3. CSV 파일은 무엇이고, Python에서 어떻게 읽을 수 있는가?
