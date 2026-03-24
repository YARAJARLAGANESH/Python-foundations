# 1. Squares of numbers
def squares(nums):
    return [x**2 for x in nums]

# 2. Even numbers only
def even_numbers(nums):
    return [x for x in nums if x % 2 == 0]

# 3. Convert strings to uppercase
def to_upper(strings):
    return [s.upper() for s in strings]

# 4. Length of each word
def word_lengths(words):
    return [len(w) for w in words]

# 5. Flatten a 2D list
def flatten(matrix):
    return [item for row in matrix for item in row]

# 6. Filter strings with length > 3
def long_words(words):
    return [w for w in words if len(w) > 3]

# 7. Replace negative numbers with 0
def replace_negative(nums):
    return [x if x >= 0 else 0 for x in nums]

# 8. Get first letters of each word
def first_letters(words):
    return [w[0] for w in words if w]

# 9. Create pairs (i, j)
def pairs(n):
    return [(i, j) for i in range(n) for j in range(n)]

# 10. Remove duplicates (preserve order)
def unique_list(nums):
    seen = set()
    return [x for x in nums if not (x in seen or seen.add(x))]

if __name__ == "__main__":
    nums = [1, -2, 3, 4, -5]
    words = ["hello", "hi", "python", "AI"]
    matrix = [[1, 2], [3, 4]]

    print(squares(nums))
    print(even_numbers(nums))
    print(to_upper(words))
    print(word_lengths(words))
    print(flatten(matrix))
    print(long_words(words))
    print(replace_negative(nums))
    print(first_letters(words))
    print(pairs(3))
    print(unique_list([1,2,2,3,1,4]))