import unittest
import sys
import os
import timeout_decorator
from participants.ctcook.fix_me_1 import add_nums
from participants.ctcook.fix_me_2 import subtract
from participants.ctcook.fix_me_3 import multiply
from participants.ctcook.fix_me_4 import divide
from participants.ctcook.fix_me_5 import square
from participants.ctcook.fix_me_6 import cube
from participants.ctcook.fix_me_7 import is_even
from participants.ctcook.fix_me_8 import is_odd
from participants.ctcook.fix_me_9 import max_of_two
from participants.ctcook.fix_me_10 import min_of_two
from participants.ctcook.fix_me_11 import modulus
from participants.ctcook.fix_me_12 import power
from participants.ctcook.fix_me_13 import absolute
from participants.ctcook.fix_me_14 import floor_divide
from participants.ctcook.fix_me_15 import negate
from participants.ctcook.fix_me_16 import remainder
from participants.ctcook.fix_me_17 import double
from participants.ctcook.fix_me_18 import triple
from participants.ctcook.fix_me_19 import square_root
from participants.ctcook.fix_me_20 import max_of_three
from participants.ctcook.fix_me_21 import min_of_three
from participants.ctcook.fix_me_22 import is_positive
from participants.ctcook.fix_me_23 import is_negative
from participants.ctcook.fix_me_24 import is_zero
from participants.ctcook.fix_me_25 import is_divisible
from participants.ctcook.fix_me_26 import is_greater
from participants.ctcook.fix_me_27 import is_less
from participants.ctcook.fix_me_28 import is_equal
from participants.ctcook.fix_me_29 import is_not_equal
from participants.ctcook.fix_me_30 import is_multiple
from participants.ctcook.fix_me_31 import is_odd_or_even
from participants.ctcook.fix_me_32 import is_positive_or_negative
from participants.ctcook.fix_me_33 import is_prime
from participants.ctcook.fix_me_34 import factorial
from participants.ctcook.fix_me_35 import fibonacci
from participants.ctcook.fix_me_36 import gcd
from participants.ctcook.fix_me_37 import lcm
from participants.ctcook.fix_me_38 import sum_of_squares
from participants.ctcook.fix_me_39 import product_of_list
from participants.ctcook.fix_me_40 import reverse_string
from participants.ctcook.fix_me_41 import palindrome_check
from participants.ctcook.fix_me_42 import count_vowels
from participants.ctcook.fix_me_43 import is_anagram
from participants.ctcook.fix_me_44 import remove_duplicates
from participants.ctcook.fix_me_45 import flatten_list
from participants.ctcook.fix_me_46 import capitalize_words
from participants.ctcook.fix_me_47 import find_max_in_list
from participants.ctcook.fix_me_48 import find_min_in_list
from participants.ctcook.fix_me_49 import sort_list
from participants.ctcook.fix_me_50 import merge_sorted_lists


class Testctcook(unittest.TestCase):
    
    @timeout_decorator.timeout(1)
    def test_add(self):
        self.assertEqual(add_nums(2, 3), 5)
        self.assertEqual(add_nums(-1, 1), 0)
        self.assertEqual(add_nums(0, 0), 0)
    
    @timeout_decorator.timeout(1)
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)
    
    @timeout_decorator.timeout(1)
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
    
    @timeout_decorator.timeout(1)
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
    
    @timeout_decorator.timeout(1)
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(0), 0)
    
    @timeout_decorator.timeout(1)
    def test_cube(self):
        self.assertEqual(cube(2), 8)
        self.assertEqual(cube(-2), -8)
        self.assertEqual(cube(0), 0)
    
    @timeout_decorator.timeout(1)
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))
    
    @timeout_decorator.timeout(1)
    def test_is_odd(self):
        self.assertFalse(is_odd(2))
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(0))
    
    @timeout_decorator.timeout(1)
    def test_max_of_two(self):
        self.assertEqual(max_of_two(2, 3), 3)
        self.assertEqual(max_of_two(5, 1), 5)
        self.assertEqual(max_of_two(-1, -5), -1)
    
    @timeout_decorator.timeout(1)
    def test_min_of_two(self):
        self.assertEqual(min_of_two(2, 3), 2)
        self.assertEqual(min_of_two(5, 1), 1)
        self.assertEqual(min_of_two(-1, -5), -5)
    
    @timeout_decorator.timeout(1)
    def test_modulus(self):
        self.assertEqual(modulus(7, 3), 1)
        self.assertEqual(modulus(8, 4), 0)
        self.assertEqual(modulus(5, 2), 1)
    
    @timeout_decorator.timeout(1)
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(power(5, 0), 1)
    
    @timeout_decorator.timeout(1)
    def test_absolute(self):
        self.assertEqual(absolute(-5), 5)
        self.assertEqual(absolute(5), 5)
    
    @timeout_decorator.timeout(1)
    def test_floor_divide(self):
        self.assertEqual(floor_divide(7, 2), 3)
        self.assertEqual(floor_divide(8, 4), 2)
        with self.assertRaises(ZeroDivisionError):
            floor_divide(5, 0)
    
    @timeout_decorator.timeout(1)
    def test_negate(self):
        self.assertEqual(negate(5), -5)
        self.assertEqual(negate(-5), 5)
        self.assertEqual(negate(0), 0)
    
    @timeout_decorator.timeout(1)
    def test_remainder(self):
        self.assertEqual(remainder(7, 3), 1)
        self.assertEqual(remainder(8, 4), 0)
        self.assertEqual(remainder(5, 2), 1)
    
    @timeout_decorator.timeout(1)
    def test_double(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(-3), -6)
        self.assertEqual(double(0), 0)
    
    @timeout_decorator.timeout(1)
    def test_triple(self):
        self.assertEqual(triple(2), 6)
        self.assertEqual(triple(-3), -9)
        self.assertEqual(triple(0), 0)
    
    @timeout_decorator.timeout(1)
    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(2), 2**0.5)
        self.assertEqual(square_root(0), 0)
    
    @timeout_decorator.timeout(1)
    def test_max_of_three(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(5, 2, 1), 5)
        self.assertEqual(max_of_three(1, 5, 2), 5)
    
    @timeout_decorator.timeout(1)
    def test_min_of_three(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(5, 2, 1), 1)
        self.assertEqual(min_of_three(1, 5, 2), 1)
    
    @timeout_decorator.timeout(1)
    def test_is_positive(self):
        self.assertTrue(is_positive(5))
        self.assertFalse(is_positive(0))
        self.assertFalse(is_positive(-5))
    
    @timeout_decorator.timeout(1)
    def test_is_negative(self):
        self.assertFalse(is_negative(5))
        self.assertFalse(is_negative(0))
        self.assertTrue(is_negative(-5))
    
    @timeout_decorator.timeout(1)
    def test_is_zero(self):
        self.assertFalse(is_zero(5))
        self.assertTrue(is_zero(0))
        self.assertFalse(is_zero(-5))
    
    @timeout_decorator.timeout(1)
    def test_is_divisible(self):
        self.assertTrue(is_divisible(6, 3))
        self.assertFalse(is_divisible(5, 2))
        self.assertTrue(is_divisible(0, 1))
    
    @timeout_decorator.timeout(1)
    def test_is_greater(self):
        self.assertTrue(is_greater(5, 3))
        self.assertFalse(is_greater(3, 5))
        self.assertFalse(is_greater(5, 5))
    
    @timeout_decorator.timeout(1)
    def test_is_less(self):
        self.assertFalse(is_less(5, 3))
        self.assertTrue(is_less(3, 5))
        self.assertFalse(is_less(5, 5))
    
    @timeout_decorator.timeout(1)
    def test_is_equal(self):
        self.assertTrue(is_equal(5, 5))
        self.assertFalse(is_equal(3, 5))
        self.assertFalse(is_equal(5, 3))
    
    @timeout_decorator.timeout(1)
    def test_is_not_equal(self):
        self.assertFalse(is_not_equal(5, 5))
        self.assertTrue(is_not_equal(3, 5))
        self.assertTrue(is_not_equal(5, 3))
    
    @timeout_decorator.timeout(1)
    def test_is_multiple(self):
        self.assertTrue(is_multiple(6, 2))
        self.assertFalse(is_multiple(5, 2))
        self.assertTrue(is_multiple(0, 5))
    
    @timeout_decorator.timeout(1)
    def test_is_odd_or_even(self):
        self.assertEqual(is_odd_or_even(2), "even")
        self.assertEqual(is_odd_or_even(3), "odd")
        self.assertEqual(is_odd_or_even(0), "even")
    
    @timeout_decorator.timeout(1)
    def test_is_positive_or_negative(self):
        self.assertEqual(is_positive_or_negative(5), "positive")
        self.assertEqual(is_positive_or_negative(-5), "negative")
        self.assertEqual(is_positive_or_negative(0), "negative")  # Assuming 0 is treated as negative
    
    @timeout_decorator.timeout(1)
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
    
    @timeout_decorator.timeout(1)
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
    
    @timeout_decorator.timeout(1)
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(6), 8)
    
    @timeout_decorator.timeout(1)
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(7, 5), 1)
    
    @timeout_decorator.timeout(1)
    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(3, 5), 15)
        self.assertEqual(lcm(2, 2), 2)
    
    @timeout_decorator.timeout(1)
    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares([1, 2, 3]), 14)
        self.assertEqual(sum_of_squares([0, 1, 2]), 5)
        self.assertEqual(sum_of_squares([]), 0)
    
    @timeout_decorator.timeout(1)
    def test_product_of_list(self):
        self.assertEqual(product_of_list([1, 2, 3]), 6)
        self.assertEqual(product_of_list([0, 1, 2]), 0)
        self.assertEqual(product_of_list([]), 0)  # Assuming empty list returns 0
    
    @timeout_decorator.timeout(1)
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
    
    @timeout_decorator.timeout(1)
    def test_palindrome_check(self):
        self.assertTrue(palindrome_check("racecar"))
        self.assertTrue(palindrome_check("level"))
        self.assertFalse(palindrome_check("hello"))
        self.assertTrue(palindrome_check(""))
        self.assertTrue(palindrome_check("a"))
    
    @timeout_decorator.timeout(1)
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("xyz"), 0)
        self.assertEqual(count_vowels(""), 0)
    
    @timeout_decorator.timeout(1)
    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("heart", "earth"))
        self.assertFalse(is_anagram("hello", "world"))
        self.assertTrue(is_anagram("", ""))
    
    @timeout_decorator.timeout(1)
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([]), [])
    
    @timeout_decorator.timeout(1)
    def test_flatten_list(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(flatten_list([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(flatten_list([]), [])
    
    @timeout_decorator.timeout(1)
    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python programming"), "Python Programming")
        self.assertEqual(capitalize_words(""), "")
    
    @timeout_decorator.timeout(1)
    def test_find_max_in_list(self):
        self.assertEqual(find_max_in_list([1, 2, 3]), 3)
        self.assertEqual(find_max_in_list([-1, -2, -3]), -1)
        with self.assertRaises(ValueError):
            find_max_in_list([])
    
    @timeout_decorator.timeout(1)
    def test_find_min_in_list(self):
        self.assertEqual(find_min_in_list([1, 2, 3]), 1)
        self.assertEqual(find_min_in_list([-1, -2, -3]), -3)
        with self.assertRaises(ValueError):
            find_min_in_list([])
    
    @timeout_decorator.timeout(1)
    def test_sort_list(self):
        self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3])
        self.assertEqual(sort_list([-1, -3, -2]), [-3, -2, -1])
        self.assertEqual(sort_list([]), [])
    
    @timeout_decorator.timeout(1)
    def test_merge_sorted_lists(self):
        self.assertEqual(merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_lists([1, 2], [3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sorted_lists([], []), [])


if __name__ == '__main__':
    unittest.main()
