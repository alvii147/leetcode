class Solution:
    def countExpandedPalindromes(self, s: str, l: int, r: int) -> int:
        '''
        Count number of palindromes formed by expanded left and right indices.
        '''

        # no more palindromes if indices are out of range
        if l < 0 or r >= len(s):
            return 0

        # no more palindromes if left and right indices don't match
        if s[l] != s[r]:
            return 0

        # if left and right indices match, add 1 to count and keep expanding
        return 1 + self.countExpandedPalindromes(s, l - 1, r + 1)

    def countSubstrings(self, s: str) -> int:
        numOfPalindromes = 0
        for i in range(len(s)):
            numOfPalindromes += self.countExpandedPalindromes(s, i, i) + self.countExpandedPalindromes(s, i, i + 1)

        return numOfPalindromes
