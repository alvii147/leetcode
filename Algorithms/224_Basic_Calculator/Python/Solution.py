OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
}

class Solution:
    def digitsToNum(self, digits) -> int:
        '''
        Converts list of digits to a number.
        If there are no digits, number returned is zero.
        '''
        if len(digits) == 0:
            return 0

        return int(''.join(digits))

    def calculateHelper(self, s: str, opening_bracket_idx: int) -> tuple[int, int]:
        '''
        Recursively calculates total starting from opening bracket index,
        returns total and closing bracket index.
        '''
        running_total = 0
        digits = []
        operator = '+'
        s_len = len(s)
        i = opening_bracket_idx

        while i < s_len:
            i += 1

            if s[i] == ' ':
                # skip if character is blank
                continue
            elif s[i] in OPERATIONS:
                # if operator found, perform operation of previous operator
                if operator is not None:
                    running_total = OPERATIONS[operator](running_total, self.digitsToNum(digits))

                digits = []
                operator = s[i]
            elif s[i].isnumeric():
                # if number found, add to digits
                digits.append(s[i])
            elif s[i] == '(':
                # if open bracket found, recursively calculate value inside brackets
                total, i = self.calculateHelper(s, i)

                if operator is not None:
                    running_total = OPERATIONS[operator](running_total, total)
                    operator = None
                else:
                    running_total = total
            elif s[i] == ')':
                # if closing bracket found, calculate running total one last time and stop
                if operator is not None:
                    running_total = OPERATIONS[operator](running_total, self.digitsToNum(digits))

                break

        return running_total, i

    def calculate(self, s: str) -> int:
        # call recursive function with surrounding brackets
        total, _ = self.calculateHelper(f'({s})', 0)

        return total
