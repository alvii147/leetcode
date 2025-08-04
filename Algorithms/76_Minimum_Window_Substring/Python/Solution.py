from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # counter for each character in current window
        window_counter = Counter()
        # counter for each character in t
        t_counter = Counter(t)
        # number of characters in t remaining
        # to be included in substring
        remaining = len(t)
        # left pointer index
        l = 0
        # left pointer index of smallest window found so far
        min_l = None
        # right pointer index of smallest window found so far
        min_r = None

        for r in range(len(s)):
            # increase window counter for current character
            window_counter[s[r]] += 1
            # if current character fulfils the need for a character in t
            # then decrement remaining characters count
            if t_counter[s[r]] >= window_counter[s[r]]:
                remaining -= 1

            # keep increasing left pointer index
            # until we have at least one remaining character
            while remaining < 1:
                # update minimum window pointers
                if min_l is None or min_r is None or r - l < min_r - min_l:
                    min_l = l
                    min_r = r

                # if left-most character is needed
                # decrement remaining count
                if t_counter[s[l]] >= window_counter[s[l]]:
                    remaining += 1

                # decrement count for character
                window_counter[s[l]] -= 1
                # increment left index pointer
                l += 1

        # if no minimum is found, no substring exists, return empty string
        if min_l is None or min_r is None:
            return ''

        return s[min_l : min_r + 1]
