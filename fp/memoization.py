from functools import lru_cache

@lru_cache
def is_palindrome(word):
    if not word:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    return False


for word in ("madam", "malayalam", "tenat"):
    if is_palindrome(word):
        print(f'\t\033[32mPASS\033[0m {word}')
    else:
        print(f'\t\033[31mFAIL\033[0m {word}')
