#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    som, i = 0, 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = len(roman_string)
    while i < n:
        a = rom_num[roman_string[i]]
        if i != n - 1:
            b = rom_num[roman_string[i + 1]]
            if a < b:
                som += (b - a)
                i += 2
                continue
        som += a
        i += 1
    return som
