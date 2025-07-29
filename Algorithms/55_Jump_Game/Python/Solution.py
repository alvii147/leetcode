from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maintain the maximum index we can jump to
        # from previous index positions
        max_idx = 0

        for idx, jump_length in enumerate(nums):
            # if maximum index falls behind current index
            # then we can never reach current index to begin with
            # which means the last index is unreachable
            if max_idx < idx:
                return False

            # update maximum index
            max_idx = max(max_idx, idx + jump_length)

        return True
