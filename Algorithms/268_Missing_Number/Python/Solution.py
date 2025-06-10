class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # if the list contained all numbers from 0 to n inclusive
        # then the expected sum of numbers would be:
        # (n + 1) / 2 [2a + n * d]
        # where a is the first element and d is the common difference of the arithmetic progression
        # a = 0 and d = 0
        # so expected sum = n * (n + 1) / 2
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        missing_number = expected_sum - actual_sum

        return missing_number
