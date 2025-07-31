import bisect

class TimeMap:
    def __init__(self):
        # initialize storage hash map
        # this stores mappings from key to list of timestamp-value pairs
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in map, assign it to a list with a single timestamp-value pair
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
            return

        # insert timestamp-value pair into sorted list
        bisect.insort(self.map[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # if key not in map, return empty string
        if key not in self.map:
            return ""

        # find maximum index i such that the timestamp at i
        # is less than or equal to the given timestamp
        i = bisect.bisect_right(self.map[key], timestamp, key=lambda x: x[0]) - 1
        # if i is negative, all timestamps are strictly higher
        # so we return empty string
        if i < 0:
            return ""

        # otherwise return the timestamp at index i
        return self.map[key][i][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
