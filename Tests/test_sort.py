import pytest
from src import my_lib


# Тест функции, проверяющей упорядоченность от минимального к максимальному во входном списке
class TestBubbleSort:

    # Выходные данные функции для выполнения теста: отсортированный по возрастанию список
    @pytest.fixture
    def sorted_example(self):
        return [1, 2, 3, 5, 132]

    # Выходные данные функции для выполнения теста: неотсортированный по возрастанию список
    @pytest.fixture
    def unsorted_example(self):
        return [1, 2, 132, 5, 3]

    # Выходные данные функции для выполнения теста: неотсортированный по возрастанию список с одинаковыми значениями
    @pytest.fixture
    def unsorted_qeual_example(self):
        return [1, 2, 132, 5, 3, 2, 123]

    # Выходные данные функции для выполнения теста: отсортированный по возрастанию список с одинаковыми значениями
    @pytest.fixture
    def sorted_qeual_example(self):
        return [1, 2, 2, 3, 5, 123, 132]

    # Тест функции на неотсортированном списке, проверка значений с сортированным списком
    def test_on_ordered(self, sorted_example, unsorted_example):
        assert my_lib.sort(unsorted_example) == sorted_example

    # Тест функции с одинаковыми значениями в списке
    def test_on_equal(self, sorted_qeual_example, unsorted_qeual_example):
        assert my_lib.sort(unsorted_qeual_example) == sorted_qeual_example
