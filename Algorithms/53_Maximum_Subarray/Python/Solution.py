class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # local maximum represents the maximum between
        # the sum of the subarray so far and the sum of starting fresh from current index
        local_max = nums[0]
        # global maximum represents maximum of all local maxima
        global_max = nums[0]

        for i in range(1, len(nums)):
            # either add to local maximum, or start fresh from current index
            local_max = max(local_max + nums[i], nums[i])
            # update global maximum
            global_max = max(global_max, local_max)

        return global_max
