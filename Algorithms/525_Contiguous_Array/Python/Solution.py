class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # current net number of ones vs zeros
        net_ones = 0
        # storage of indices of earliest occurrences of net ones vs zeros
        # start with {0: -1} because at index -1 (i.e. before the list begins) net ones vs zeros is balanced
        net_ones_occurrences = {0: -1}
        # current running maximum length
        max_length = 0

        for i, num in enumerate(nums):
            # update current net ones vs zeros
            net_ones += -1 if num == 0 else num

            # if net ones vs zeros has been seen before
            # distance between current index and where it was seen before
            # is potential maximum length
            if net_ones in net_ones_occurrences:
                max_length = max(max_length, i - net_ones_occurrences[net_ones])
                continue

            # store new net ones vs zeros occurrence index
            net_ones_occurrences[net_ones] = i

        return max_length
