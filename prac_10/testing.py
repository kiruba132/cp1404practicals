"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('this is a test')
    'This is a test.'
    """
    phrase = phrase.capitalize()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # Assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Test if the Car's odometer is set correctly
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Test if the Car's fuel is set correctly with a given value
    test_car_with_fuel = Car(fuel=10)
    assert test_car_with_fuel.fuel == 10, "Car does not set fuel correctly when provided"

    # Test if the Car's fuel is set correctly with the default value
    default_fuel_car = Car()
    assert default_fuel_car.fuel == 0, "Car does not set fuel correctly when not provided"

    # Uncomment the following line to run doctests
    doctest.testmod()


run_tests()