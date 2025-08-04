class Solution:
    def reverseBits(self, n: int) -> int:
        # start with zero
        reversed_n = 0

        # iterate over 32 bits
        for _ in range(32):
            # left shift to make space for new bit
            reversed_n <<= 1
            # add new bit
            reversed_n += n % 2
            # right shift n to get next bit
            n >>= 1

        return reversed_n
