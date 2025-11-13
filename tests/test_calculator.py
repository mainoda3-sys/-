"""
Calculator 모듈 테스트
Tests for Calculator Module
"""

import unittest
import sys
import os

# src 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Calculator 클래스 테스트"""
    
    def setUp(self):
        """각 테스트 전에 실행"""
        self.calc = Calculator()
    
    def test_add(self):
        """덧셈 테스트"""
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """뺄셈 테스트"""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_multiply(self):
        """곱셈 테스트"""
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_divide(self):
        """나눗셈 테스트"""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=5)
    
    def test_divide_by_zero(self):
        """0으로 나누기 예외 테스트"""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
