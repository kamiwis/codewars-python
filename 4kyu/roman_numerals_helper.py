# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Input range : 1 <= n < 4000

# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
# Examples

# RomanNumerals.to_roman(1000) # should return 'M'
# RomanNumerals.from_roman('M') # should return 1000


# My Solution
import math
class RomanNumerals:

    def to_roman(val):
        num_to_roman = {1: "I", 4: "IV", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        roman_str = ""
        value = val
        while value > 0:
            if value >= 1000:
                roman_str += "M"
                value -= 1000
            elif value >= 900:
                roman_str += "CM"
                value -= 900
            elif value >= 500:
                roman_str += "D"
                value -= 500
            elif value >= 400:
                roman_str += "CD"
                value -= 400
            elif value >= 100:
                roman_str += "C"
                value -= 100
            elif value >= 90:
                roman_str += "XC"
                value -= 90
            elif value >= 50:
                roman_str += "L"
                value -= 50
            elif value >= 40:
                roman_str += "XL"
                value -= 40
            elif value >= 10:
                roman_str += "X"
                value -= 10
            elif value >= 9:
                roman_str += "IX"
                value -= 9
            elif value >= 5:
                roman_str += "V"
                value -= 5
            elif value >= 4:
                roman_str += "IV"
                value -= 4
            elif value >= 1:
                roman_str += "I"
                value -= 1
        return roman_str

    def from_roman(roman_num):
        roman_to_num = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD':400, 'CM': 900}
        value = 0
        roman = roman_num
        while len(roman) > 0:
            if roman[0:2] in roman_to_num:
                value += roman_to_num[roman[0:2]]
                roman = roman.replace(roman[0:2], "", 1)
            else:
                value += roman_to_num[roman[0]]
                roman = roman.replace(roman[0], "", 1)
        return value