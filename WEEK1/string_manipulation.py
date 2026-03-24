# 1. Convert string to uppercase
def to_upper(s):
    return s.upper()

# 2. Convert string to lowercase
def to_lower(s):
    return s.lower()

# 3. Reverse a string
def reverse_string(s):
    return s[::-1]

# 4. Check palindrome
def is_palindrome(s):
    return s == s[::-1]

# 5. Count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

# 6. Remove spaces
def remove_spaces(s):
    return s.replace(" ", "")

# 7. Count words
def count_words(s):
    return len(s.split())

# 8. Capitalize first letter of each word
def capitalize_words(s):
    return s.title()

# 9. Find frequency of characters
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# 10. Replace a word in string
def replace_word(s, old, new):
    return s.replace(old, new)

if __name__ == "__main__":
    s = "hello world"

    print(to_upper(s))
    print(to_lower(s))
    print(reverse_string(s))
    print(is_palindrome("madam"))
    print(count_vowels(s))
    print(remove_spaces(s))
    print(count_words(s))
    print(capitalize_words(s))
    print(char_frequency(s))
    print(replace_word(s, "world", "Python"))