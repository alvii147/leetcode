import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain min heap of numbers
        min_heap = []

        for num in nums:
            # add number to min heap
            heapq.heappush(min_heap, num)

            # pop from min heap until we have exactly k numbers
            while len(min_heap) > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)
