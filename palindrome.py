def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (same forwards and backwards).
    Example:
        is_palindrome("madam") -> True
    """
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]


# Demo usage
if __name__ == "__main__":
    print(is_palindrome("Madam"))          # True
    print(is_palindrome("Hello"))          # False
    print(is_palindrome("A man a plan Panama"))  # True
