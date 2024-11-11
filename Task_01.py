def is_palindrome(s):
    if s == (None):
        return False
    elif isinstance(s, (int, float)):
        ss = str()
        for i in str(s):
            ss += i
            cleaned_string = ''.join(char for char in ss)
        return cleaned_string == cleaned_string[::-1]
    else:
        cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
        if cleaned_string.isalnum():
            return cleaned_string == cleaned_string[::-1]
        return False


print(is_palindrome("A man, a plan, a canal -- Panama"))  # => True
print(is_palindrome("Madam, I'm Adam!"))  # => True
print(is_palindrome(333))  # => True
print(is_palindrome(None))  # => False
print(is_palindrome("Abracadabra"))  # => False
print(is_palindrome("  "))  # => False
