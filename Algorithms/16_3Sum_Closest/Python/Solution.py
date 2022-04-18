class Solution:
    # get sum in pair that's closest to target
    def getClosestSumInPair(self, sum1: int, sum2: int, target: int) -> int:
        if abs(target - sum1) < abs(target - sum2):
            return sum1

        return sum2

    # get closest two sum
    def twoSumClosest(self, target: int, j: int, k: int) -> int:
        currentSum = self.nums_sorted[j] + self.nums_sorted[k]
        # base case: if j and k are consecutive
        if j + 1 == k or currentSum == target:
            return currentSum

        # if current sum is lower than target, increment j and recurse
        if currentSum < target:
            nextSum = self.twoSumClosest(target, j + 1, k)
        # if current sum is higher than target, decrement k and recurse
        elif currentSum > target:
            nextSum = self.twoSumClosest(target, j, k - 1)
        # if current sum is target, return current sum
        else:
            return currentSum

        # get closest sum in pair
        closestSum = self.getClosestSumInPair(currentSum, nextSum, target)

        return closestSum

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort nums
        self.nums_sorted = sorted(nums)
        nums_len = len(nums)
        closestSum = None

        for i in range(len(self.nums_sorted) - 2):
            # if current and previous indices hold same values, skip this loop
            # if the values are same, this loop is redundant
            if i > 0 and self.nums_sorted[i - 1] == self.nums_sorted[i]:
                continue

            # choose i as current index and get two sum closest
            twoSum = self.twoSumClosest(target - self.nums_sorted[i], i + 1, nums_len - 1)
            if closestSum is None:
                closestSum = twoSum + self.nums_sorted[i]
            else:
                closestSum = self.getClosestSumInPair(closestSum, twoSum + self.nums_sorted[i], target)

        return closestSum
