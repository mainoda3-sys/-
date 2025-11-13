"""
간단한 계산기 모듈
Simple Calculator Module
"""


class Calculator:
    """기본 계산 연산을 수행하는 계산기 클래스"""
    
    def add(self, a, b):
        """두 숫자를 더합니다."""
        return a + b
    
    def subtract(self, a, b):
        """두 숫자를 뺍니다."""
        return a - b
    
    def multiply(self, a, b):
        """두 숫자를 곱합니다."""
        return a * b
    
    def divide(self, a, b):
        """두 숫자를 나눕니다."""
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return a / b


def main():
    """메인 함수 - 계산기 사용 예제"""
    calc = Calculator()
    
    print("=== 계산기 예제 ===")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    
    # 0으로 나누기 예외 처리
    try:
        result = calc.divide(10, 0)
    except ValueError as e:
        print(f"에러: {e}")


if __name__ == "__main__":
    main()
