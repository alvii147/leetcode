class Solution:
    def maxArea(self, height: List[int]) -> int:
        # current max area
        maxAreaValue = 0
        # left index
        i = 0
        # right index
        j = len(height) - 1
        # while left and right index haven't crossed each other
        while i < j:
            # calculate area
            area = (j - i) * min(height[i], height[j])
            # update max area
            maxAreaValue = max(maxAreaValue, area)

            # if left height is smaller, increment left index
            if height[i] < height[j]:
                i += 1
            # otherwise, decrement right index
            else:
                j -= 1

        # return max area
        return maxAreaValue
