class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if only one element exists, that's the minimum
        if len(nums) == 1:
            return nums[0]

        # if left-most element is less than right-most element
        # then the list has not been rotated
        # (or it has been rotated a multiple of n times)
        # in which case the left-most element is the minimum
        if nums[0] < nums[-1]:
            return nums[0]

        # maintain left and right indices for binary search
        left_idx = 0
        right_idx = len(nums)
        # maintain minimum value found so far
        min_val = None

        # keep iterating until left and right indices meet
        while left_idx < right_idx:
            # compute mid point of left and right indices
            mid_idx = (left_idx + right_idx) // 2

            # if element at mid point is lower than current minimum, record it
            if min_val is None or min_val > nums[mid_idx]:
                min_val = nums[mid_idx]

            # if element at mid point is higher than left-most element
            # then we haven't yet reached the discontinuity in the sorted list
            # and we should search in the right-half of the list
            # otherwise, we have already passed the discontinuity in the sorted list
            # in which case we should search in the left-half of the list
            if nums[mid_idx] > nums[0]:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx

        return min_val
