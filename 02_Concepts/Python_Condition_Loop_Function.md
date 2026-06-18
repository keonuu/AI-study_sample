# Python 조건문, 반복문, 함수

Tags: `Python`, `Conditional`, `Loop`, `Function`, `QC`, `Beginner`

## Summary

Python에서 조건문은 조건에 따라 다른 코드를 실행하고, 반복문은 여러 값을 하나씩 처리하며, 함수는 자주 쓰는 판단이나 계산을 이름 붙여 재사용하게 한다. `if / elif / else`는 위에서부터 조건을 검사하고 처음 맞는 조건 하나만 실행하므로, 조건의 순서가 중요하다.

## Conditional Statement

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

읽는 방법:

```text
mapping_rate가 0.8 이상이면 pass를 출력한다.
그렇지 않으면 fail을 출력한다.
```

## Comparison Operators

자주 쓰는 비교 연산자:

```text
>=  크거나 같다
>   크다
<=  작거나 같다
<   작다
==  같다
!=  같지 않다
```

주의할 점:

```python
if mapping_rate = 0.8:
```

위 코드는 틀린 코드다. `=`는 값을 저장할 때 쓰고, 같은지 비교할 때는 `==`를 쓴다.

```python
if mapping_rate == 0.8:
```

## if / elif / else

조건이 여러 단계일 때는 `elif`를 사용한다.

```python
def check_qc(rate):
    if rate >= 0.9:
        return "excellent"
    elif rate >= 0.8:
        return "pass"
    else:
        return "fail"
```

판단 결과:

```text
0.95 -> excellent
0.85 -> pass
0.72 -> fail
```

핵심:

```text
위에서부터 검사한다.
처음 맞는 조건 하나만 실행한다.
그 아래 조건은 더 이상 보지 않는다.
```

## Condition Order Matters

아래 코드는 좋은 분류 코드가 아니다.

```python
def check_qc(rate):
    if rate >= 0.8:
        return "pass"
    elif rate >= 0.9:
        return "excellent"
    else:
        return "fail"
```

`0.92`는 `0.8` 이상이므로 첫 번째 조건에서 바로 `"pass"`가 반환된다. 따라서 아래의 `elif rate >= 0.9`는 실행될 기회가 없다.

좋은 순서:

```python
def check_qc(rate):
    if rate >= 0.9:
        return "excellent"
    elif rate >= 0.8:
        return "pass"
    else:
        return "fail"
```

더 엄격한 조건을 위에 두면 의도한 대로 분류할 수 있다.

## For Loop

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

읽는 방법:

```text
samples 안에서 값을 하나씩 꺼낸다.
꺼낸 값을 sample이라는 이름으로 잠시 부른다.
매번 print(sample)을 실행한다.
```

## Function

함수는 자주 쓰는 판단이나 계산을 이름 붙여 저장한 코드 묶음이다.

```python
def check_qc(rate):
    if rate >= 0.8:
        return "pass"
    else:
        return "fail"
```

사용:

```python
result = check_qc(0.76)
print(result)
```

출력:

```text
fail
```

읽는 방법:

```text
check_qc 함수에 0.76을 넣는다.
함수 안에서는 rate가 0.76이 된다.
0.76은 0.8 이상이 아니므로 fail을 반환한다.
그 결과가 result에 저장된다.
print(result)가 화면에 fail을 출력한다.
```

## return vs print

`return`:

```text
함수의 결과를 밖으로 돌려준다.
```

`print()`:

```text
값을 화면에 보여준다.
```

둘은 다르다. 함수 안에서 결과를 계산해 나중에 다시 쓰려면 `return`이 필요하다.

## Sample QC Example

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

## Indentation

Python에서는 들여쓰기가 코드의 소속을 결정한다.

```python
if mapping_rate >= 0.8:
    print("pass")
```

위 코드에서 `print("pass")`는 `if` 조건이 맞을 때만 실행된다.

들여쓰기가 사라지면 의미가 달라진다.

```python
if mapping_rate >= 0.8:
    result = "pass"

print(result)
```

`print(result)`는 `if` 바깥에 있으므로 조건문이 끝난 뒤 실행된다.

## Bioinformatics Context

실제 bioinformatics 분석에서는 QC 기준을 이런 식으로 코드로 표현할 수 있다.

```text
mapping_rate >= 0.9 -> excellent
mapping_rate >= 0.8 -> pass
mapping_rate < 0.8  -> fail
```

다만 실제 연구에서는 기준값을 임의로 정하면 안 된다. 분석 방법, 데이터 종류, 실험 목적, 논문 또는 pipeline 문서의 기준에 따라 QC 기준을 정해야 한다.
