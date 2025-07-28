class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals by right limit
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        # right limit of first interval
        right_limit = sorted_intervals[0][1]
        # total number of intervals removed
        removed_intervals = 0

        for i in range(1, len(sorted_intervals)):
            # if current interval overlaps with previous one
            # then remove current interval
            if sorted_intervals[i][0] < right_limit:
                removed_intervals += 1
                continue

            # update right limit
            right_limit = sorted_intervals[i][1]

        return removed_intervals
