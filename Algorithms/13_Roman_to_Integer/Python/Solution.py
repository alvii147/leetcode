class Solution:
    def __init__(self):
        # single digit roman numbers
        self.symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        # double digit roman numbers
        self.double_symbols = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }

    def romanToInt(self, s: str) -> int:
        # converted integer
        integer = 0
        i = 0
        while i < len(s):
            # raise error if unknown symbol found
            if s[i] not in self.symbols:
                raise ValueError(f'Invalid character {s[i]}')

            # if last element, add current character value
            if i == len(s) - 1:
                integer += self.symbols[s[i]]
                break

            # raise error if unknown symbol found for next character
            if s[i + 1] not in self.symbols:
                raise ValueError(f'Invalid character {s[i + 1]}')

            # if current character value is higher or equal to next
            # then add current character value
            if self.symbols[s[i]] >= self.symbols[s[i + 1]]:
                integer += self.symbols[s[i]]
                i += 1
                continue

            # raise error if unknown current and next character
            if s[i] + s[i + 1] not in self.double_symbols:
                raise ValueError(f'Invalid characters {s[i] + s[i + 1]}')

            # add character values for current and next character
            integer += self.double_symbols[s[i] + s[i + 1]]
            i += 2

        return integer
