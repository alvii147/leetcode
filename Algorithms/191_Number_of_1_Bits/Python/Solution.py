class Solution:
    def hammingWeight(self, n: int) -> int:
        # maintain count of set bits
        ones = 0

        while n > 0:
            # increment count of set bits if last bit is set
            ones += n % 2
            # right shift n to get next bit
            n >>= 1

        return ones
