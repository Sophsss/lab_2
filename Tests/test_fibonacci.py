from src import my_lib


# Тест функции, находящей последовательность фибоначчи
class TestFibonacci:
    # Тест программы на корректных данных
    def test_on_correct_n(self):
        assert my_lib.fibonacci(7) == [1, 1, 2, 3, 5, 8, 13]

    # Тест программы на некорректных данных
    def test_on_incorrect(self):
        # При подаче на вход программы числа 0 или отрицательного - программа должна вернуть пустой список
        assert my_lib.fibonacci(0) == []
