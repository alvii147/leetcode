class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # maintain dictionary mapping sorted string to list of grouped anagrams
        groups = {}

        # iterate over strings
        for s in strs:
            # sort string
            sorted_s = str(sorted(s))

            # if sorted string is already in groups mapping,
            # then we've already encountered an anagram of the current string
            # so we simply add to the existing list
            if sorted_s in groups:
                groups[sorted_s].append(s)
                continue

            # otherwise, create a group list for anagrams of the current string
            groups[sorted_s] = [s]

        # return list of values anagram groups
        return list(groups.values())
