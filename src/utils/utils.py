import string


def is_palindrome(text: str) -> bool:
    cleaned = ''.join(text.split()).lower()
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'ą', 'ę', 'ó'}
    return sum(1 for char in text.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def word_frequencies(text: str) -> dict:
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    
    words = cleaned_text.split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    
    return frequencies


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True
