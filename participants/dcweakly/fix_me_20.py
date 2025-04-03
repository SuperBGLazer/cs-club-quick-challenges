def max_of_three(a, b, c):
    return c if a < c and b < c else b if b > c and b > a else c
