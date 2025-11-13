# 코딩 예제 (Coding Example)

간단한 계산기를 구현한 Python 코딩 예제입니다.

## 프로젝트 구조

```
.
├── src/
│   ├── __init__.py
│   └── calculator.py      # 계산기 모듈
├── tests/
│   ├── __init__.py
│   └── test_calculator.py # 단위 테스트
└── README.md
```

## 기능

- 덧셈 (Addition)
- 뺄셈 (Subtraction)
- 곱셈 (Multiplication)
- 나눗셈 (Division)
- 0으로 나누기 예외 처리

## 사용 방법

### 계산기 실행

```bash
python src/calculator.py
```

### 테스트 실행

```bash
python -m unittest tests/test_calculator.py
```

또는 모든 테스트 실행:

```bash
python -m unittest discover tests
```

## 예제 코드

```python
from src.calculator import Calculator

calc = Calculator()

# 기본 연산
result = calc.add(10, 5)      # 15
result = calc.subtract(10, 5)  # 5
result = calc.multiply(10, 5)  # 50
result = calc.divide(10, 5)    # 2.0
```

## 요구사항

- Python 3.6 이상
