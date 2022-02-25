class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if both string and pattern are empty, return True
        if len(s) < 1 and len(p) < 1:
            return True
        # if string is non-empty and pattern is empty, return False
        elif len(p) < 1:
            return False

        # detect if next character is '*'
        if len(p) > 1 and p[1] == '*':
            i = 0
            # iterate over matches for '*'
            while i < len(s) + 1:
                # if current character does not match with character preceding '*', break out of loop
                if i > 0 and s[i - 1] != p[0] and p[0] != '.':
                    break

                # recursive call to match rest of the string
                cond = self.isMatch(s[i:], p[2:])
                if cond:
                    return True

                i += 1
        else:
            # next character is not '*', so if string is empty here, return False
            if len(s) < 1:
                return False

            # check if current characters match, then recursive call to match rest of the string
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])

        return False
