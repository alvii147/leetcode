from bisect import bisect_left

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # handle corner case of having no intervals
        if len(intervals) == 0:
            return [newInterval]

        merged_intervals = []
        # find index where the new interval would be inserted
        insertion_idx = bisect_left(intervals, newInterval[0], key=lambda interval: interval[0])

        # for all index before the insertion index,
        # we can simply insert them since they are sorted
        # and non-overlapping
        for i in range(insertion_idx - 1):
            merged_intervals.append(intervals[i])

        # start with interval at insertion index
        # or the new interval
        # depending on which comes first
        left, right = newInterval
        if insertion_idx > 0:
            left, right = intervals[insertion_idx - 1]

        # combine the insertion and new intervals if possible
        if newInterval[0] <= right:
            # if it overlaps with the new interval
            # then expand the right limit
            right = max(right, newInterval[1])
        else:
            # otherwise insert the interval
            merged_intervals.append([left, right])
            left, right = newInterval

        # insert the rest of the intervals
        for i in range(insertion_idx, len(intervals)):
            # if the current limits overlap with the current interval
            # then expand the right limit
            if intervals[i][0] <= right:
                right = max(right, intervals[i][1])
                continue

            # otherwise insert the interval
            merged_intervals.append([left, right])
            left, right = intervals[i]

        # insert the last remaining interval
        merged_intervals.append([left, right])

        return merged_intervals
