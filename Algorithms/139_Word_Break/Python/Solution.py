from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dictionary that maps indices in s to the lengths of words that can be placed in that index
        # for e.g. if s = "cats" and wordDict = ["cat", "cats", "at"], then we would have {0: {3, 4}, 1: {2}}.
        wordSearches = {}
        s_len = len(s)

        # iterate over word dictionary and store occurrences of words in s
        for word in wordDict:
            word_len = len(word)

            for i in range(s_len - word_len + 1):
                if word == s[i : i + word_len]:
                    if i not in wordSearches:
                        wordSearches[i] = {word_len}
                    else:
                        wordSearches[i].add(word_len)

        # queue for the index to start with
        queueIdx = deque([0])
        # set to hold indices that have already been explored
        visitedIdx = {0}

        # keep reading from queue until all items exhaused
        while len(queueIdx) > 0:
            idx = queueIdx.popleft()

            # iterate over all word lengths that fit in current index
            for wordLen in wordSearches.get(idx, []):
                nextIdx = idx + wordLen

                # can't consider word if it causes us to go over length of s
                if nextIdx > s_len:
                    continue

                # if placing this words makes us reach the finish line
                # then we CAN segment s into given words
                if nextIdx == s_len:
                    return True

                # skip if next index already visited
                if nextIdx in visitedIdx:
                    continue

                # mark next index as visited
                visitedIdx.add(nextIdx)
                # add next index to queue
                queueIdx.append(nextIdx)

        # if loop exits, we have exhausted all options
        # meaning we CANNOT segment s into given words
        return False
