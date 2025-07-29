class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by left limit
        intervals.sort()
        # start with the first interval
        interval = [intervals[0][0], intervals[0][1]]
        merged_intervals = []

        for i in range(1, len(intervals)):
            # if current interval and stored interval are overlapping
            # then extend the stored interval
            if interval[1] >= intervals[i][0]:
                interval[1] = max(interval[1], intervals[i][1])
                continue

            # otherwise add to the merged intervals
            # and store current interval
            merged_intervals.append(interval)
            interval = [intervals[i][0], intervals[i][1]]

        # add the last remaining interval
        merged_intervals.append(interval)

        return merged_intervals
