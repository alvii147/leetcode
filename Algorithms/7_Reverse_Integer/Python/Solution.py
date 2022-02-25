class Solution:
    def reverse(self, x: int) -> int:
        # get value and sign of number
        num = x
        sign = -1 if num < 0 else 1
        # reversed number
        reversed_num = 0
        # int 32 max value
        int32_max = 2147483647

        while num:
            # get units digit
            remainder = num % 10
            # floor divide by 10 to shift digits to right
            quotient = num // 10

            # sign is negative, adjust remainder and quotient
            if sign == -1:
                remainder = (10 - remainder) % 10
                if remainder != 0:
                    quotient += 1

            # check for possible overflow, return 0 if so
            if (int32_max - remainder) / 10 < reversed_num:
                return 0

            # multiply by 10 to shift digits to left
            reversed_num *= 10
            # add remainder
            reversed_num += remainder
            # update number to be quotient
            num = quotient

        # update sign of reversed number
        reversed_num *= sign

        return reversed_num
