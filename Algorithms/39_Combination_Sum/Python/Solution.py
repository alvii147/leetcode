class Solution:
    def combinationSumHelper(
        self,
        candidates_used: list[int],
        candidates_available: list[int],
        remaining: int,
    ) -> list[list[int]]:
        '''
        Assuming the list of candidates is sorted,
        recursively compute all the combinations
        that sum up to the remaining amount.
        '''
        # if remaining amount is zero, there is only one combination
        if remaining == 0:
            return [candidates_used]

        combs = []
        # iterate over each available candidate
        for i, c in enumerate(candidates_available):
            # if candidate's value is higher than remaining, we can stop
            if c > remaining:
                break

            # start with candidate frequency of 1
            freq = 1
            # keep increasing the frequency of the candidate's appearance
            # until we can't anymore, upon which we move on to the next candidate
            while True:
                if c * freq > remaining:
                    break

                combs += self.combinationSumHelper(
                    candidates_used + ([c] * freq),
                    candidates_available[i + 1:],
                    remaining - (c * freq),
                )

                freq += 1

        return combs

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort candidates so we can stop when the candidate gets larger than the target
        candidates = sorted(candidates)

        return self.combinationSumHelper([], candidates, target)
