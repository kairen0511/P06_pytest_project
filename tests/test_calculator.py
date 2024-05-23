from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 123
        b = 45
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 5535
        assert result == expected

    def test_divide(self):
        # arrange
        a = 144
        b = 12
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 12
        assert result == expected

        # Test division by zero
        b = 0
        try:
            result = cal.divide(a, b)
            assert False, "Expected an exception for division by zero"
        except ZeroDivisionError:
            pass
