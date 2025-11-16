from utils.utils import is_palindrome


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

