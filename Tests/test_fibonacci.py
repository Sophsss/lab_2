import my_lib
import pytest


class TestFibonacci:

    def test_on_correct_n(self):
        assert my_lib.fibonacci(7) == [1, 1, 2, 3, 5, 8, 13]

    def test_on_incorrect(self):
        assert my_lib.fibonacci(0) == []
