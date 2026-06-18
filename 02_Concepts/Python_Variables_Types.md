# Python 변수와 기본 자료형

Tags: `Python`, `Variable`, `Type`, `List`, `Dictionary`, `Beginner`

## Summary

Python에서 변수는 값에 붙이는 이름표다. `print(변수)`는 변수 안의 값을 출력하고, `print("글자")`는 따옴표 안의 글자 자체를 출력한다. Python의 기본 자료형에는 `str`, `int`, `float`, `bool`, `list`, `dict`가 있다.

## Running Python On This Computer

현재 PowerShell에서는 `python` 명령어가 인식되지 않았고, Windows Python launcher인 `py`가 동작했다.

Python 버전:

```text
Python 3.13.5
```

Python 파일 실행:

```powershell
py 03_Python_Practice\day05_variables.py
```

## Variable

변수는 값에 붙이는 이름표다.

```python
gene_name = "TP53"
read_count = 1520
```

읽는 방법:

```text
gene_name이라는 이름표에 "TP53"을 저장한다.
read_count라는 이름표에 1520을 저장한다.
```

## print

변수 안의 값을 출력:

```python
gene = "BRCA1"
print(gene)
```

출력:

```text
BRCA1
```

글자 자체를 출력:

```python
print("gene")
```

출력:

```text
gene
```

핵심 차이:

```text
print(gene)   -> gene 변수 안의 값 출력
print("gene") -> "gene"이라는 글자 출력
```

## Basic Types

```python
sample_id = "S01"
read_count = 35000
mapping_rate = 0.87
passed_qc = True
```

자료형:

```text
sample_id: str
read_count: int
mapping_rate: float
passed_qc: bool
```

Python에서 실제 자료형 이름:

```text
string  -> str
integer -> int
float   -> float
boolean -> bool
```

## type

`type()`은 값의 자료형을 확인한다.

```python
print(type(sample_id))
print(type(read_count))
print(type(mapping_rate))
print(type(passed_qc))
```

출력은 대략 다음과 같다.

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

## List

`list`는 여러 값을 순서대로 담는 자료형이다.

```python
genes = ["TP53", "BRCA1", "EGFR"]
```

읽는 방법:

```text
genes라는 변수 안에 유전자 이름 3개를 순서대로 담았다.
```

## Dictionary

`dictionary`, 줄여서 `dict`는 key와 value를 짝으로 저장하는 자료형이다.

```python
sample = {
    "sample_id": "S01",
    "condition": "treated",
    "cell_line": "HEK293",
    "read_count": 35000,
    "mapping_rate": 0.87,
}
```

읽는 방법:

```text
sample_id는 S01
condition은 treated
cell_line은 HEK293
read_count는 35000
mapping_rate는 0.87
```

값 꺼내기:

```python
print(sample["condition"])
```

출력:

```text
treated
```

## List vs Dictionary

List:

```python
sample = ["S01", "treated", "HEK293", 35000, 0.87]
```

특징:

```text
값들이 순서대로 들어 있지만, 각 값의 의미를 순서로 기억해야 한다.
```

Dictionary:

```python
sample = {
    "sample_id": "S01",
    "condition": "treated",
    "cell_line": "HEK293",
    "read_count": 35000,
    "mapping_rate": 0.87,
}
```

특징:

```text
각 값에 이름표가 붙어 있어서 의미가 명확하다.
```

정리:

```text
list = 여러 값을 순서대로 단순 나열
dict = 각 정보에 이름표를 붙여 의미까지 함께 저장
```

## One-Line Dictionary vs Multi-Line Dictionary

짧은 dictionary는 한 줄로 써도 된다.

```python
sample = {"sample_id": "S01", "condition": "treated"}
```

정보가 많아지면 여러 줄로 쓰는 편이 읽기 좋다.

```python
sample = {
    "sample_id": "S01",
    "condition": "treated",
}
```

여러 줄로 쓰면 사람이 읽기 쉽고, Git에서 어떤 줄이 바뀌었는지도 확인하기 쉽다.

## NameError And Case Sensitivity

Python은 이름을 정확히 구분한다.

```python
gene = "TP53"

print(gene)
print(Gene)
```

`gene`과 `Gene`은 서로 다른 이름이다. 위 코드에서 `Gene`은 정의된 적이 없으므로 `NameError`가 난다.

핵심:

```text
Python에서 변수 이름은 정확히 일치해야 한다.
대소문자도 구분한다.
```

