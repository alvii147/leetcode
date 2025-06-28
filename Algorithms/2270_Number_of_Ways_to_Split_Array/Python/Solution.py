class Solution:
    def cumulativeSum(self, nums: List[int]) -> List[int]:
        '''
        Calculate cumulative sum of list.
        '''
        nums_len = len(nums)
        cum_sum_nums = [0] * nums_len
        cum_sum_nums[0] = nums[0]

        for i in range(1, nums_len):
            cum_sum_nums[i] = nums[i] + cum_sum_nums[i - 1]

        return cum_sum_nums

    def waysToSplitArray(self, nums: List[int]) -> int:
        cum_sum_nums = self.cumulativeSum(nums)
        num_of_ways = 0

        for i in range(len(nums) - 1):
            # if sum of left side is greater than or equal to sum of right side
            # then we have found a way to split
            if cum_sum_nums[i] >= cum_sum_nums[-1] - cum_sum_nums[i]:
                num_of_ways += 1

        return num_of_ways
