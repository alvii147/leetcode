class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Rotated array can be broken down into left and right sides.
        # For example, if [0, 1, 2, 4, 5, 6, 7] is rotated at pivot index 3,
        # then we have [4, 5, 6, 7, 0, 1, 2].
        # Here, [4, 5, 6, 7] is the left side and [0, 1, 2] is the right side.
        # If target >= 4, then it will be on the left side.
        # Otherwise, it will be on the right side.

        # find out whether the target is on the left or right side
        target_left_side = True
        if target < nums[0]:
            target_left_side = False

        # begin binary search with left and right indices
        i = 0
        j = len(nums)
        # iterate until left and right indices overlap
        while i < j:
            # get mid point index
            m = (i + j) // 2

            # if we found the target, return it as we're done
            if nums[m] == target:
                return m

            if target_left_side:
                if nums[m] <= nums[0] or nums[m] > target:
                    # if target is on left side,
                    # and either, mid point is on the right side,
                    # or mid point is higher than target,
                    # then we should discard the right side
                    # and continue searching on the left side
                    j = m
                else:
                    # otherwise, discard the left side
                    # and continue searching on the right side
                    i = m + 1
            else:
                if nums[m] >= nums[0] or nums[m] < target:
                    # if target is on the right side,
                    # and either, mid point is on the left side,
                    # or mid point is lower than target,
                    # then we should discard the left side
                    # and continue searching on the right side
                    i = m + 1
                else:
                    # otherwise, discard the right side
                    # and continue search on the left side
                    j = m

        # if we have exhausted our binary search without finding the target
        # then the target doesn't exist
        return -1
