from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        # create a counter of characters in p for comparisons
        p_counter = Counter(p)
        # create a counter of p_len characters in s for comparisons
        s_window_counter = Counter(s[:p_len])
        # maintain list of anagram indices
        anagram_indices = []

        # iterate over sliding windows
        for i in range(s_len - p_len + 1):
            # window is already set on first iteration
            if i != 0:
                # remove left-most element from counter
                s_window_counter[s[i - 1]] -= 1
                # add right-most element to counter
                s_window_counter[s[i + p_len - 1]] += 1

            # check if current window is an anagram
            if s_window_counter == p_counter:
                anagram_indices.append(i)

        return anagram_indices
