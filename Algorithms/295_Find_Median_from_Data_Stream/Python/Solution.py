from numbers import Number
from heapq import heappush, heappop


def minheappush(h: list[Number], num: Number) -> None:
    """
    Push a number onto a min heap.
    """
    heappush(h, num)

def minheappop(h: list[Number]) -> Number:
    """
    Pop a number from a min heap.
    """
    return heappop(h)

def minheappeak(h: list[Number]) -> Number | None:
    """
    Peak the minimum value of a min heap without popping it.
    Returns None if the heap is empty.
    """
    if len(h) == 0:
        return None

    return h[0]

def maxheappush(h: list[Number], num: Number) -> None:
    """
    Push a number onto a max heap.
    """
    heappush(h, -num)

def maxheappop(h: list[Number]) -> Number:
    """
    Pop a number from a max heap.
    """
    return -heappop(h)

def maxheappeak(h: list[Number]) -> Number:
    """
    Peak the maximum value of a max heap without popping it.
    Returns None if the heap is empty.
    """
    if len(h) == 0:
        return None

    return -h[0]

class MedianFinder:
    def __init__(self):
        # min heap to store the large half of numbers
        self.large_nums = []
        # max heap to store the small half of numbers
        self.small_nums = []

    def push_large(self, num: int) -> None:
        """
        Push a number onto the min heap of large numbers.
        """
        minheappush(self.large_nums, num)

    def pop_large(self) -> int:
        """
        Pop a number from the min heap of large numbers.
        """
        return minheappop(self.large_nums)

    def peak_large(self) -> int | None:
        """
        Peak the minimum number from the min heap of large numbers.
        """
        return minheappeak(self.large_nums)

    def len_large(self) -> int:
        """
        Get the length of the min heap of large numbers.
        """
        return len(self.large_nums)

    def push_small(self, num: int) -> None:
        """
        Push a number onto the max heap of small numbers.
        """
        maxheappush(self.small_nums, num)

    def pop_small(self) -> int:
        """
        Pop a number from the max heap of small numbers.
        """
        return maxheappop(self.small_nums)

    def peak_small(self) -> int | None:
        """
        Peak the maximum number from the max heap of small numbers.
        """
        return maxheappeak(self.small_nums)

    def len_small(self) -> int:
        """
        Get the length of the max heap of small numbers.
        """
        return len(self.small_nums)

    def balance(self):
        """
        Balance the large and small heaps.
        They must either have the same number of elements,
        or the large heap must have one extra element.
        """
        # Keep popping from large heap and pushing to small heap
        # until large heap is at a capacity that is
        # at most one higher than the small heap.
        while self.len_large() - self.len_small() > 1:
            self.push_small(self.pop_large())

        # Keep popping from large heap and pushing to small heap
        # until large heap is at a capacity that is
        # at most one higher than the small heap.
        while self.len_small() - self.len_large() > 0:
            self.push_large(self.pop_small())

    def addNum(self, num: int) -> None:
        """
        Add number for median calculation.
        """
        # If the large heap is empty, or if given number
        # is higher than or equal to smallest number in the large heap,
        # then add it to the large heap.
        # Otherwise, add it to the small heap.
        min_large = self.peak_large()
        if min_large is None or num >= min_large:
            self.push_large(num)
        else:
            self.push_small(num)

        # balance heaps after addition
        self.balance()

    def findMedian(self) -> float:
        """
        Get the median of the added numbers.
        """
        # If balanced, the large heap is guaranteed to have
        # at most one more element than the small heap,
        # or at least equal number of elements.
        # If they have equal number of elements, total number
        # of elements is even, and we take average of the middle values.
        if self.len_large() == self.len_small():
            return (self.peak_large() + self.peak_small()) / 2

        # Otherwise, smallest value of the large heap is median
        return self.peak_large()


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
