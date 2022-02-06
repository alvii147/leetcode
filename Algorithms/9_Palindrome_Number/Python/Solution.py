class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        # return False if negative
        if num < 0:
            return False

        # list to store digits
        digits = []
        while num > 0:
            # append remainder to digits list
            digits.append(num % 10)
            # set number to quotient
            num = num // 10

        # left iterator
        i = 0
        # right iterator
        j = len(digits) - 1
        while i < j:
            # if left & right elements are not equal, return False
            if digits[i] != digits[j]:
                return False
            # increment left iterator
            i += 1
            # decrement right iterator
            j -= 1

        return True