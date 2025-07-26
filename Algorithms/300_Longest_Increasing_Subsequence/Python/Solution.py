class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # maintain list of longest increasing subsequences
        # that end at the number at each index
        # initialized at 1, since every number can be its own subsequence
        lis = [1] * len(nums)
        # maintain the maximum length of increasing subsequence seen so far
        max_lis = 1
        # iterate over every index
        for i in range(len(nums)):
            # iterate over every index on the left
            for j in range(i):
                # if nums[j] is less than nums[i]
                # then the longest subsequence at j can be extended
                # by adding nums[i] to the end
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
                    max_lis = max(max_lis, lis[i])

        return max_lis
