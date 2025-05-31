class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set of numbers
        nums_set = set(nums)
        # initialize list of starting numbers
        # a number n is a starting number if n is in the set but n - 1 isn't
        starting_nums_set = []

        # iterate over set of numbers and find starting numbers
        for num in nums_set:
            if num - 1 not in nums_set:
                starting_nums_set.append(num)

        # iterate over starting numbers
        # and count how many consequtive numbers belong to the set
        # maintain the maximum sequence length and return that as answer
        max_seq_len = 0
        for starting_num in starting_nums_set:
            seq_len = 1
            num = starting_num + 1
            while num in nums_set:
                seq_len += 1
                num += 1

            max_seq_len = max(max_seq_len, seq_len)

        return max_seq_len
