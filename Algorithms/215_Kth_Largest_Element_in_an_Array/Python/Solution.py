import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain max heap of numbers
        maxHeap = []

        for num in nums:
            # add number to max heap
            # by default, heapq implements min heap
            # so we negate the numbers to make it a max heap
            heapq.heappush(maxHeap, -num)

        # pop the top k numbers from the heap
        for _ in range(k):
            kthLargest = -heapq.heappop(maxHeap)

        return kthLargest
