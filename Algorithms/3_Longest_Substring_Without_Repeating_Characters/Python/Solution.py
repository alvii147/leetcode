class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dictionary that maps character to its index in string
        char_indices = {}
        # index of starting character of current substring
        substr_start_idx = 0
        # length of current substring
        substr_len = 0
        # maximum length of substrings seen so far
        max_substr_len = 0

        for i, c in enumerate(s):
            # check if current character has appeared before
            # set -1 has default so we skip the if condition that follows
            repeated_char_idx = char_indices.get(c, -1)
            if repeated_char_idx >= substr_start_idx:
                # update maximum length so far
                max_substr_len = max(max_substr_len, substr_len)
                # new substring should start from index after previously repeated character
                substr_start_idx = repeated_char_idx + 1
                # new length spans from character after previously repeated character to current character
                substr_len = i - repeated_char_idx
                # store character and index in dictionary
                char_indices[c] = i
                continue

            # increment substring length
            substr_len += 1
            # store character and index in dictionary
            char_indices[c] = i

        # update maximum length one last time
        # needed in case final substring did not encounter repeated character
        max_substr_len = max(max_substr_len, substr_len)

        return max_substr_len
