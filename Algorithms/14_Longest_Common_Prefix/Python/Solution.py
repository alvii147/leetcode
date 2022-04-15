class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # character iteration index
        i = 0
        # longest common prefix
        prefix = ''

        while True:
            # common letter
            letter = ''
            # condition on if all letters at position are common
            common = True

            for s in strs:
                # if end of string, break
                if i >= len(s):
                    common = False
                    break

                # if letter is empty, add letter
                if len(letter) < 1:
                    letter = s[i]
                    continue

                # if letter is the same, continue
                if s[i] == letter:
                    continue

                # otherwise, letters are not common, break
                common = False
                break

            # if letters are not common, break
            if not common:
                break

            # otherwise add common letter to prefix
            prefix += letter
            i += 1

        return prefix
