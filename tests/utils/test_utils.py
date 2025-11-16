from utils.utils import is_palindrome, fibonacci, count_vowels
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
