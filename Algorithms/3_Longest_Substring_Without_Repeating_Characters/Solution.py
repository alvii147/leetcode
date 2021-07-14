class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left & right iterators
        i = 0
        j = 0
        # dictionary to store substring 
        char_hash = {}
        # length of longest substring
        max_len = 0

        while j < len(s):
            # if new character is already in hash
            if s[j] in char_hash:
                # delete characters from hash
                k = char_hash[s[j]] + 1
                for l in s[i:k]:
                    del char_hash[l]

                # move left iterator
                i = k

            # add new character to hash
            char_hash[s[j]] = j
            # increment right iterator
            j += 1

            # check if current substring is longer than previous maximum
            if max_len < j - i:
                max_len = j - i

        return max_len