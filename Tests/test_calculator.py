from src import my_lib
import pytest

# Тест функции, вычисляющий значение выражений
class TestCalculator:
    # Тест операции сложения на корректных данных
    def test_add_on_correct(self):
        assert my_lib.calculator(100, 21, "+") == 121

    # Тест операции вычитания на корректных данных
    def test_subtract_on_correct(self):
        assert my_lib.calculator(30, 12, "-") == 18

    # Тест операции умножения на корректных данных
    def test_multiply_on_correct(self):
        assert my_lib.calculator(6, 6, "*") == 36

    # Тест операции деления на корректных данных
    def test_divide_on_correct(self):
        assert my_lib.calculator(10, 5, "/") == 2

    # Тест операции деления на некорректных данных, выхываем исключение
    def test_dived_on_zero(self):
        with pytest.raises(ZeroDivisionError):
            my_lib.calculator(10, 0, "/")
