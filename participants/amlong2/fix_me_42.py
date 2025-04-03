def count_vowels(s):
    return len(list(filter(lambda x: x in "aeiou", s)))
