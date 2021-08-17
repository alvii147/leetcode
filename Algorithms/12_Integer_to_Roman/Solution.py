class Solution:
    # roman numeral characters
    numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'V̅', 'X̅']

    # get characters within decade
    def getNumerals(self, power: int) -> List[str]:
        return self.numerals[power * 2 : (power * 2) + 3]

    # get roman digit given value and decade characters
    def getDigit(self, digit: int, one: str, five: str, ten: str) -> str:
        if digit < 1:
            return ''
        elif digit < 4:
            return one * digit
        elif digit == 4:
            return one + five
        elif digit < 9:
            return five + (one * (digit - 5))
        elif digit == 9:
            return one + ten
        else:
            return ten

    # convert integer to roman numerals
    def intToRoman(self, num: int) -> str:
        # remaining value
        val = num
        # power of current digit
        power = 0
        # final roman number
        romanNumber = ''

        # while there remains a value
        while(val > 0):
            # get units digit
            digit = val % 10
            # shift digits in value
            val = val // 10

            # get roman numeral characters for current power
            numeralsList = self.getNumerals(power)
            # get roman digit given current units digit
            romanDigit = self.getDigit(digit, *numeralsList)
            # concatenate roman digit with final roman number
            romanNumber = romanDigit + romanNumber

            # increment power
            power += 1

        return romanNumber