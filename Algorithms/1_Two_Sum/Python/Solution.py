class Solution:
    # sort list by index
    def argsort(self, nums: List[int]) -> List[int]:
        sorted_args = [i[0] for i in sorted(enumerate(nums), key=lambda x:x[1])]

        return sorted_args

    # compute 2Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # get indices of sorted nums
        nums_argsort = self.argsort(nums)
        # get sorted nums
        nums_sort = [nums[i] for i in nums_argsort]

        forward_iter = 0
        backward_iter = len(nums_sort) - 1
        while(forward_iter < backward_iter):
            # if numbers add up to target, return indices
            if nums_sort[forward_iter] + nums_sort[backward_iter] == target:
                return nums_argsort[forward_iter], nums_argsort[backward_iter]

            # if addition is short of target, increment forward iterator
            if nums_sort[backward_iter] + nums_sort[forward_iter] < target:
                forward_iter += 1
            # else, if addition is higher than target, decrement backward iterator
            else:
                backward_iter -= 1

        raise ValueError('No solution exists for given list.')