from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # left index
        l = 0
        # right index
        r = 0
        # counter to keep track of the number of characters in current window
        counter = Counter()

        # keep iterating until right index reaches end of string
        while r < len(s):
            # increment right index of window
            r += 1
            # increment counter of new character added by expanding right index
            counter[s[r - 1]] += 1

            # if performing character replacement of the most common character k times
            # is not enough to make the entire window into the most common character,
            # then we should advance the left index to remove the first character in
            # the window
            if counter.most_common(1)[0][1] + k < r - l:
                # increment left index of window
                l += 1
                # decrement counter of character removed by advancing left index
                counter[s[l - 1]] -= 1

        # final window length is the longest repeated character string we can achieve
        return r - l
