#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = None

    for letter in roman_string:
        if letter not in roman_values:
            return 0

        curr_value = roman_values[letter]
        if prev_value and prev_value < curr_value:
            result -= prev_value
            curr_value -= prev_value

        result += curr_value
        prev_value = curr_value

    return result
