class Solution:
    def rob(self, nums: List[int]) -> int:
       # we maintain two maximums:
        # * the maximum we can get if we choose the current number
        # * the maximum we can get if we DON'T choose the current number
        max_if_chosen = 0
        max_if_not_chosen = 0

        for num in nums:
            # at every iteration, we update the maximums:
            # * maximum if we choose current number is
            #   current number + maximum we get if we DON'T choose the last number
            # * maximum if we DON'T choose current number is
            #   maximum between what we get if we DO OR DON'T choose the last number
            max_if_chosen, max_if_not_chosen = (
                num + max_if_not_chosen,
                max(max_if_chosen, max_if_not_chosen),
            )

        return max(max_if_chosen, max_if_not_chosen)
