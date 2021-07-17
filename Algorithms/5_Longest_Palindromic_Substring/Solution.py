class Solution:
    # get length of longest palindrome by expanding indices outwards
    def expandedPalindromeLength(self, s, i: int, j: int) -> int:
        n = len(s)

        # if indices hit limits, return 0
        if i < 0 or j > n - 1:
            return 0

        # if value at indices are equal
        if s[i] == s[j]:
            added_length = 1 if i == j else 2
            # expand indices outwards
            return added_length + self.expandedPalindromeLength(s, i - 1, j + 1)

        # if value at indices are not equal, return 0
        return 0

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxPalindrome = ''

        # if string has only one character, return the whole string
        if s == len(s) * s[0]:
            return s

        for k in range(n):
            # get maximum expanded palindrome length for each index and index pairs
            m = max(
                self.expandedPalindromeLength(s, k, k),
                self.expandedPalindromeLength(s, k, k + 1)
            )

            # if expanded palindrome length is higher than current palindrome length, update max palindrome
            if m > len(maxPalindrome):
                maxPalindrome = s[k - ((m - 1) // 2):k + ((m + 2) // 2)]

        return maxPalindrome