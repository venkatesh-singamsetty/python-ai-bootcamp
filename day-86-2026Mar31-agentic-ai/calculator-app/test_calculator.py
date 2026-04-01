"""
Unit tests for the Calculator application
"""
import pytest
from calculatory import add, subtract, multiply, divide


class TestCalculator:
    """Test cases for calculator functions"""
    
    def test_add(self):
        """Test addition operation"""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(1.5, 2.5) == 4.0
        
    def test_subtract(self):
        """Test subtraction operation"""
        assert subtract(5, 3) == 2
        assert subtract(10, 5) == 5
        assert subtract(0, 0) == 0
        assert subtract(-1, -1) == 0
        
    def test_multiply(self):
        """Test multiplication operation"""
        assert multiply(2, 3) == 6
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6
        assert multiply(1.5, 2) == 3.0
        
    def test_divide(self):
        """Test division operation"""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
        assert divide(5, 2) == 2.5
        
    def test_divide_by_zero(self):
        """Test division by zero returns error message"""
        result = divide(10, 0)
        assert result == "Error! Division by zero."
        
    def test_divide_negative(self):
        """Test division with negative numbers"""
        assert divide(-10, 2) == -5
        assert divide(10, -2) == -5
        assert divide(-10, -2) == 5


class TestCalculatorIntegration:
    """Integration tests for the calculator"""
    
    def test_multiple_operations(self):
        """Test chaining multiple operations"""
        result = add(multiply(2, 3), subtract(10, 5))
        assert result == 11  # (2*3) + (10-5) = 6 + 5 = 11
        
    def test_complex_expression(self):
        """Test complex mathematical expression"""
        # (15 + 5) * 2 / 4 = 20 * 2 / 4 = 40 / 4 = 10
        result = divide(multiply(add(15, 5), 2), 4)
        assert result == 10


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
