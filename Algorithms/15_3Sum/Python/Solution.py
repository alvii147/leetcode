class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        nums_sorted = sorted(nums)
        triplets = []

        for i in range(nums_len):
            # if i-th & (i - 1)th elements are equal, increment i and continue
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue

            # left most element on the right of i
            j = i + 1
            # right most element on the right of i
            k = nums_len - 1

            while j < k:
                # if j-th & (j - 1)th elements are equal, increment j and continue
                if j > i + 1 and nums_sorted[j] == nums_sorted[j - 1]:
                    j += 1
                    continue

                triplet = [nums_sorted[i], nums_sorted[j], nums_sorted[k]]
                nums_sum = sum(triplet)
                # if sum smaller than target, move left index forward
                if nums_sum < 0:
                    j += 1
                # if sum larger than target, move right index backward
                elif nums_sum > 0:
                    k -= 1
                # if target sum achieved, record triplet & move both indices
                else:
                    triplets.append(triplet)
                    j += 1
                    k -= 1

        return triplets
