def count_vowels(s):
    return len(filter(s, lambda x: x in "aeiou"))
