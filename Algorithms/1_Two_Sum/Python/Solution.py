class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary that maps number to its index in the list
        nums_indices = {}

        for i, num in enumerate(nums):
            # if number that adds current number to target exists
            # then return their indices
            diff_num = target - num
            if diff_num in nums_indices:
                return [i, nums_indices[diff_num]]

            nums_indices[num] = i

        raise ValueError('No two sum pair found')
