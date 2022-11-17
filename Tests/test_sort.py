import pytest
import my_lib


class TestBubbleSort:

    @pytest.fixture
    def sorted_example(self):
        return [2, 3, 11, 14, 32]

    @pytest.fixture
    def unsorted_example(self):
        return [11, 2, 32, 14, 3]

    @pytest.fixture
    def unsorted_qeual_example(self):
        return [11, 2, 32, 14, 3, 11, 32]

    @pytest.fixture
    def sorted_qeual_example(self):
        return [2, 3, 11, 11, 14, 32, 32]

    def test_on_ordered(self, sorted_example, unsorted_example):
        assert my_lib.sort(unsorted_example) == sorted_example

    def test_on_equal(self, sorted_qeual_example, unsorted_qeual_example):
        assert my_lib.sort(unsorted_qeual_example) == sorted_qeual_example
