# Day 05 - Python 기초 1: 변수, 자료형, 실행

## Today's Goal

Python 파일을 실행하고, 변수와 기본 자료형을 이해한다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 5를 따른다.

## Work Log

- PowerShell에서 `python --version`은 인식되지 않았지만, `py --version`은 정상 동작했다.
- 현재 Python 실행 명령어는 `py`를 사용한다.
- Python 파일은 `.py` 확장자를 가진 파일이다.
- `print()`는 화면에 값을 출력하는 함수다.
- 변수는 값에 붙이는 이름표라고 이해했다.
- `print(sample_name)`은 변수 안의 값을 출력하고, `print("sample_name")`은 글자 자체를 출력한다.
- `str`, `int`, `float`, `bool` 기본 자료형을 구분했다.
- `list`는 여러 값을 순서대로 담고, `dict`는 key와 value를 짝으로 담는 자료형임을 배웠다.
- dictionary는 단순 값뿐 아니라 각 값의 의미를 이름표와 함께 저장할 때 유용하다.
- Python은 변수 이름의 오타와 대소문자를 엄격하게 구분한다.

## Environment Check

PowerShell에서 `python` 명령어는 인식되지 않았다.

```powershell
python --version
```

대신 Windows Python launcher인 `py`가 동작했다.

```powershell
py --version
```

확인된 버전:

```text
Python 3.13.5
```

따라서 현재 실습에서는 다음 명령어를 사용한다.

```powershell
py 03_Python_Practice\day05_variables.py
```

## Concepts Learned

### Variable

변수는 값에 붙이는 이름표다.

```python
gene_name = "TP53"
read_count = 1520
```

### print

```python
print(gene_name)
```

위 코드는 `gene_name`이라는 변수 안에 들어 있는 값을 출력한다.

```python
print("gene_name")
```

위 코드는 `"gene_name"`이라는 글자 자체를 출력한다.

### Basic Types

```python
sample_id = "S01"       # str
read_count = 35000      # int
mapping_rate = 0.87     # float
passed_qc = True        # bool
```

### List

`list`는 여러 값을 순서대로 담는다.

```python
genes = ["TP53", "BRCA1", "EGFR"]
```

### Dictionary

`dict`는 key와 value를 짝으로 저장한다.

```python
sample = {
    "sample_id": "S01",
    "condition": "treated",
    "cell_line": "HEK293",
    "read_count": 35000,
    "mapping_rate": 0.87,
}
```

값을 꺼낼 때는 다음처럼 쓴다.

```python
print(sample["condition"])
```

출력:

```text
treated
```

## Practice File

오늘 만든 Python 실습 파일:

```text
03_Python_Practice\day05_variables.py
```

실행 명령어:

```powershell
py 03_Python_Practice\day05_variables.py
```

## Common Mistakes

### Variable Name vs String

```python
print(gene)
```

변수 `gene` 안의 값을 출력한다.

```python
print("gene")
```

`gene`이라는 글자 자체를 출력한다.

### Dictionary Key Access

틀린 예:

```python
print(condition)
```

이 코드는 `condition`이라는 변수를 찾으려 한다.

맞는 예:

```python
print(sample["condition"])
```

이 코드는 `sample` dictionary 안에서 `"condition"` key에 해당하는 값을 꺼낸다.

### Typo And Case Sensitivity

```python
print(smaple["read_count"])
```

`sample`을 `smaple`로 잘못 쓴 오타다. Python은 추측하지 않으므로 `NameError`가 난다.

```python
gene = "TP53"
print(Gene)
```

`gene`과 `Gene`은 서로 다른 이름이다. Python은 대소문자를 구분한다.

## LLM Wiki Note Candidate

Title: Python 변수와 기본 자료형

Tags: `Python`, `Variable`, `Type`, `List`, `Dictionary`, `Beginner`

Summary:

Python에서 변수는 값에 붙이는 이름표다. `print(변수)`는 변수 안의 값을 출력하고, `print("글자")`는 글자 자체를 출력한다. 기본 자료형에는 `str`, `int`, `float`, `bool`이 있으며, `list`는 여러 값을 순서대로 담고, `dict`는 key와 value를 짝으로 저장한다.

## Questions For Next Time

1. 조건문은 왜 필요한가?
2. 반복문은 어떤 상황에서 쓰는가?
3. 함수를 쓰면 무엇이 좋아지는가?
