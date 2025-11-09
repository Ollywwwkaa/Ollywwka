def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]
print(is_palindrome("топот"))
print(is_palindrome("python"))