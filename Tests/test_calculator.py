import my_lib
import pytest


class TestCalculator:

    def test_add_on_correct(self):
        assert my_lib.calculator(51, 27, "+") == 78

    def test_subtract_on_correct(self):
        assert my_lib.calculator(25, 11, "-") == 14

    def test_multiply_on_correct(self):
        assert my_lib.calculator(5, 6, "*") == 30

    def test_divide_on_correct(self):
        assert my_lib.calculator(5, 1, "/") == 5

    def test_dived_on_zero(self):
        with pytest.raises(ZeroDivisionError):
            my_lib.calculator(5, 0, "/")
