class Solution:
    # slice string based on index-based condition
    def slicer(self, s: str, index: 'Callable[[int], bool]') -> str:
        return ''.join([c for i, c in enumerate(s) if index(i)])

    def convert(self, s: str, numRows: int) -> str:
        # return string if numRows is 1 to avoid zero division error
        if numRows < 2:
            return s

        # index divisor
        divisor = (numRows - 1) * 2
        zigzag = ''
        for j in range(numRows):
            # slice list for each line
            zigzag += self.slicer(s, index = lambda x: (x - j) % divisor == 0 or (x + j) % divisor == 0)

        return zigzag