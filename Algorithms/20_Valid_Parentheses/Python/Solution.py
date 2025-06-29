from collections import deque

# set of opening parentheses
PARENTHESES_OPENERS = {'(','{','['}

# mapping from closing to opening parentheses
PARENTHESES_PAIRS_MAP = {
    ')': '(',
    '}': '{',
    ']': '[',
}

class Solution:
    def isValid(self, s: str) -> bool:
        # create a stack
        stack = deque()
        # iterate over string
        for c in s:
            # if parenthesis is opener
            # add to stack and continue
            if c in PARENTHESES_OPENERS:
                stack.append(c)
                continue

            # otherwise check if closing parenthesis matches the opener on top of stack
            # if not, string is not valid
            if len(stack) == 0 or stack.pop() != PARENTHESES_PAIRS_MAP[c]:
                return False

        # string is only valid if no parentheses remain in stack
        return len(stack) == 0
