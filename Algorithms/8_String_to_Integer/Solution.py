class Solution:
    def myAtoi(self, s: str) -> int:
        # converted integer
        num = 0
        # sign of number
        sign = 1
        # int 32 max value
        int32_max = 2147483647
        # int 32 min value
        int32_min = -2147483648

        for i, c in enumerate(s.lstrip()):
            # check for negative sign
            if c == '-':
                # if not first, break loop
                if i != 0:
                    break
                # set negative sign
                sign = -1
            elif c == '+':
                # if not first, break loop
                if i != 0:
                    break
                # set positive sign
                sign = 1
            else:
                # if non-numeric, break loop
                if not c.isnumeric():
                    break

                # check for possible overflow
                if (int32_max - int(c)) / 10 < num:
                    # if sign is negative, return int32 min
                    if sign == -1:
                        return int32_min
                    # otherwise return int32 max
                    else:
                        return int32_max

                # multiply by 10 to shift digits to left
                num *= 10
                # add digit
                num += int(c)

        # update sign
        num *= sign

        return num