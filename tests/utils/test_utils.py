from utils.utils import is_palindrome, fibonacci, count_vowels, calculate_discount, flatten_list
import pytest


class TestIsPalindrome:

    def test_kajak(self):
        assert is_palindrome("kajak") is True

    def test_kobyla_ma_maly_bok(self):
        assert is_palindrome("Kobyła ma mały bok") is True

    def test_python(self):
        assert is_palindrome("python") is False

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_single_character(self):
        assert is_palindrome("A") is True


class TestFibonacci:

    def test_fibonacci_0(self):
        assert fibonacci(0) == 0

    def test_fibonacci_1(self):
        assert fibonacci(1) == 1

    def test_fibonacci_5(self):
        assert fibonacci(5) == 5

    def test_fibonacci_10(self):
        assert fibonacci(10) == 55

    def test_fibonacci_negative(self):
        with pytest.raises(ValueError):
            fibonacci(-1)


class TestCountVowels:

    def test_python(self):
        assert count_vowels("Python") == 2

    def test_aeiouy(self):
        assert count_vowels("AEIOUY") == 6

    def test_bcd(self):
        assert count_vowels("bcd") == 0

    def test_empty_string(self):
        assert count_vowels("") == 0

    def test_polish_text(self):
        assert count_vowels("Próba żółwia") == 5


class TestCalculateDiscount:

    def test_discount_20_percent(self):
        assert calculate_discount(100, 0.2) == 80.0

    def test_discount_zero(self):
        assert calculate_discount(50, 0) == 50.0

    def test_discount_full(self):
        assert calculate_discount(200, 1) == 0.0

    def test_discount_negative(self):
        with pytest.raises(ValueError):
            calculate_discount(100, -0.1)

    def test_discount_over_one(self):
        with pytest.raises(ValueError):
            calculate_discount(100, 1.5)


class TestFlattenList:

    def test_already_flat(self):
        assert flatten_list([1, 2, 3]) == [1, 2, 3]

    def test_nested_lists(self):
        assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]

    def test_empty_list(self):
        assert flatten_list([]) == []

    def test_deeply_nested(self):
        assert flatten_list([[[1]]]) == [1]

    def test_progressively_nested(self):
        assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
